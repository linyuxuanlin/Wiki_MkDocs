#!/usr/bin/env python3
"""Repair deterministic same-site Markdown link problems.

Two classes of defects are handled without touching visible prose:
1. known historical wiki-power.com paths that were renamed or consolidated;
2. translated files whose Markdown link structure still matches the zh source,
   but whose internal URL destinations were translated by the language model.

Translations with known structural omissions are reported but never guessed at.
Any new structural mismatch remains a hard failure.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit, urlunsplit

DOCS_DIR = Path("docs")
SOURCE_DIR = DOCS_DIR / "zh"
LOCALE_DIRS = (DOCS_DIR / "en", DOCS_DIR / "es", DOCS_DIR / "ar")
SITE_HOSTS = {"wiki-power.com", "www.wiki-power.com"}

# Exact historical routes that have clear current replacements.
STALE_PATH_REPLACEMENTS = {
    "/PCB布线规范": "/个人PCB设计规范/",
    "/PCB元件布局规范": "/个人PCB设计规范/",
    "/DC-IDD_Test": "/IDD_Test/",
    "/HAL库开发笔记（二）-GPIO": "/HAL库开发笔记-GPIO/",
    "/Docker简易指南": "/Docker基础知识/",
    "/DockerCompose-更优雅的打开方式": "/DockerCompose-镜像编排工具/",
    "/史密斯圆图基础": "/史密斯圆图与匹配电路基础/",
    "/使用Markdown进行高效写作": "/使用Markdown高效写作/",
    "/基于acme.sh自动申请域名证书（群晖Docker）": "/使用acme.sh自动申请域名证书（群晖Docker）/",
    "/基于Bitwarden搭建密码管理器（群晖Docker）": "/使用Bitwarden搭建密码管理器（群晖Docker）/",
}

# These pre-existing machine translations are already structurally incomplete
# relative to the zh source. They are intentionally not repaired by ordinal
# alignment because doing so could connect the wrong translated label to a URL.
# The allowlist is exact so any *new* structural mismatch still fails CI.
KNOWN_STRUCTURAL_MISMATCHES = {
    "docs/ar/Docker基础知识.md",
    "docs/es/HAL库开发笔记-USB通信.md",
    "docs/es/Homelab-影视媒体服务器Jellyfin.md",
    "docs/ar/Homelab-影视媒体服务器Jellyfin.md",
    "docs/ar/Homelab-自托管密码管理器Vaultwarden.md",
    "docs/es/PlatformIO搭配CubeMX食用.md",
    "docs/ar/PlatformIO搭配CubeMX食用.md",
    "docs/ar/RobotCtrl_Func-外设拓展板.md",
    "docs/ar/STM32F4硬件开发.md",
    "docs/ar/为什么你需要一个知识库.md",
    "docs/es/如何用Markdown写公众号文章.md",
    "docs/es/用群晖自带反向代理实现HTTPS访问.md",
}


@dataclass(frozen=True)
class Destination:
    start: int
    end: int
    value: str


def markdown_destinations(text: str) -> list[Destination]:
    """Return inline Markdown link/image destinations with balanced parentheses."""
    results: list[Destination] = []
    cursor = 0

    while True:
        marker = text.find("](", cursor)
        if marker < 0:
            break

        start = marker + 2
        index = start
        depth = 0
        escaped = False

        while index < len(text):
            char = text[index]
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == "(":
                depth += 1
            elif char == ")":
                if depth == 0:
                    results.append(Destination(start, index, text[start:index]))
                    index += 1
                    break
                depth -= 1
            elif char == "\n" and depth == 0:
                break
            index += 1

        cursor = max(index, marker + 2)

    return results


def is_same_site_destination(value: str) -> bool:
    value = value.strip()
    if not value:
        return False
    if any(char.isspace() for char in value):
        # Skip optional Markdown titles; preserving ambiguous syntax is safer.
        return False
    if value.startswith("/") and not value.startswith("//"):
        return True
    parts = urlsplit(value)
    return parts.scheme in {"http", "https"} and parts.netloc.lower() in SITE_HOSTS


def internal_destinations(text: str) -> list[Destination]:
    return [item for item in markdown_destinations(text) if is_same_site_destination(item.value)]


def normalized_site_path(value: str) -> str | None:
    value = value.strip()
    if not is_same_site_destination(value):
        return None

    parts = urlsplit(value)
    path = unquote(parts.path or "/")
    if not path.startswith("/"):
        path = "/" + path
    if path != "/":
        path = path.rstrip("/")
    return path


def replace_destination(text: str, replacements: list[tuple[int, int, str]]) -> str:
    output = text
    for start, end, value in reversed(replacements):
        output = output[:start] + value + output[end:]
    return output


def canonicalize_known_stale_destinations(text: str) -> tuple[str, int]:
    replacements: list[tuple[int, int, str]] = []

    for item in markdown_destinations(text):
        path = normalized_site_path(item.value)
        target_path = STALE_PATH_REPLACEMENTS.get(path or "")
        if not target_path:
            continue

        parts = urlsplit(item.value.strip())
        if parts.scheme in {"http", "https"}:
            replacement = urlunsplit(
                (parts.scheme, "wiki-power.com", target_path, parts.query, parts.fragment)
            )
        else:
            replacement = target_path
            if parts.query:
                replacement += "?" + parts.query
            if parts.fragment:
                replacement += "#" + parts.fragment

        if replacement != item.value:
            replacements.append((item.start, item.end, replacement))

    return replace_destination(text, replacements), len(replacements)


def align_internal_destinations(source: str, translated: str) -> tuple[str, int, str | None]:
    source_links = internal_destinations(source)
    translated_links = internal_destinations(translated)

    if len(source_links) != len(translated_links):
        return (
            translated,
            0,
            f"internal-link count mismatch: source={len(source_links)}, translated={len(translated_links)}",
        )

    replacements: list[tuple[int, int, str]] = []
    for source_link, translated_link in zip(source_links, translated_links):
        if source_link.value == translated_link.value:
            continue
        replacements.append((translated_link.start, translated_link.end, source_link.value))

    return replace_destination(translated, replacements), len(replacements), None


def normalize_stale_links(check_only: bool) -> tuple[int, int, list[str]]:
    files_checked = 0
    changed_destinations = 0
    issues: list[str] = []

    for path in sorted(DOCS_DIR.rglob("*.md")):
        files_checked += 1
        text = path.read_text(encoding="utf-8")
        repaired, changed = canonicalize_known_stale_destinations(text)
        if not changed:
            continue

        changed_destinations += changed
        if check_only:
            issues.append(f"{path}: {changed} known stale internal destination(s)")
        else:
            path.write_text(repaired, encoding="utf-8")

    return files_checked, changed_destinations, issues


def align_translated_links(check_only: bool) -> tuple[int, int, list[str], list[str]]:
    files_checked = 0
    destinations_changed = 0
    issues: list[str] = []
    warnings: list[str] = []

    for source_path in sorted(SOURCE_DIR.glob("*.md")):
        source_text = source_path.read_text(encoding="utf-8")
        for locale_dir in LOCALE_DIRS:
            translated_path = locale_dir / source_path.name
            if not translated_path.is_file():
                continue

            files_checked += 1
            translated_text = translated_path.read_text(encoding="utf-8")
            repaired, changed, issue = align_internal_destinations(source_text, translated_text)
            if issue:
                message = f"{translated_path}: {issue}"
                key = translated_path.as_posix()
                if key in KNOWN_STRUCTURAL_MISMATCHES:
                    warnings.append(message)
                else:
                    issues.append(message)
                continue

            if not changed:
                continue

            destinations_changed += changed
            if check_only:
                issues.append(
                    f"{translated_path}: {changed} translated internal destination(s) differ from zh source"
                )
            else:
                translated_path.write_text(repaired, encoding="utf-8")

    return files_checked, destinations_changed, issues, warnings


def synthetic_tests() -> list[str]:
    errors: list[str] = []

    source = (
        "[中文标题](https://wiki-power.com/搭建属于自己的HomeLab)\n"
        "![图](https://media.wiki-power.com/img/example.png)\n"
        "[嵌套](https://wiki-power.com/TheHdw(The_Hardware)/)\n"
        "[外链](https://example.com/中文)\n"
    )
    translated = (
        "[HomeLab](https://wiki-power.com/Setting-Up-Your-Own-HomeLab)\n"
        "![Image](https://media.wiki-power.com/img/example.png)\n"
        "[Nested](https://wiki-power.com/TheHdw-The-Hardware/)\n"
        "[External](https://example.com/english)\n"
    )
    repaired, changed, issue = align_internal_destinations(source, translated)
    if issue:
        errors.append(f"synthetic alignment unexpectedly failed: {issue}")
    if changed != 2:
        errors.append(f"synthetic alignment changed {changed} destinations instead of 2")
    if "https://wiki-power.com/搭建属于自己的HomeLab" not in repaired:
        errors.append("translated same-site URL was not restored")
    if "https://wiki-power.com/TheHdw(The_Hardware)/" not in repaired:
        errors.append("balanced-parenthesis URL was not restored")
    if "https://example.com/english" not in repaired:
        errors.append("external translated URL was unexpectedly changed")
    if "https://media.wiki-power.com/img/example.png" not in repaired:
        errors.append("external media image URL was unexpectedly changed")

    stale = (
        "[旧标题](https://wiki-power.com/Docker简易指南/) "
        "[相对旧标题](/DC-IDD_Test) "
        "[外链](https://example.com/Docker简易指南/)"
    )
    stale_repaired, stale_changed = canonicalize_known_stale_destinations(stale)
    if stale_changed != 2:
        errors.append(f"stale-link test changed {stale_changed} destinations instead of 2")
    if "https://wiki-power.com/Docker基础知识/" not in stale_repaired:
        errors.append("absolute stale wiki route was not normalized")
    if "](/IDD_Test/)" not in stale_repaired:
        errors.append("root-relative stale wiki route was not normalized")
    if "https://example.com/Docker简易指南/" not in stale_repaired:
        errors.append("external stale-looking URL was unexpectedly changed")

    mismatch_result = align_internal_destinations(
        "[一](https://wiki-power.com/one) [二](https://wiki-power.com/two)",
        "[One](https://wiki-power.com/one)",
    )
    if mismatch_result[2] is None or mismatch_result[1] != 0:
        errors.append("structural mismatch was guessed instead of rejected")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="report deterministic repairs that are still needed instead of writing them",
    )
    args = parser.parse_args()

    test_errors = synthetic_tests()
    if test_errors:
        for error in test_errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 2

    docs_checked, stale_changed, stale_issues = normalize_stale_links(args.check)
    translated_checked, translated_changed, translated_issues, warnings = align_translated_links(
        args.check
    )

    mode = "check" if args.check else "repair"
    print(
        f"Internal link {mode}: checked {docs_checked} Markdown files for stale routes "
        f"and {translated_checked} translated files for URL drift; "
        f"{stale_changed} stale destination(s) and {translated_changed} translated destination(s) "
        f"{'would change' if args.check else 'repaired'}."
    )

    if warnings:
        print(
            f"Known structurally incomplete translations left untouched: {len(warnings)}",
            file=sys.stderr,
        )
        for warning in warnings:
            print(f" ~ {warning}", file=sys.stderr)

    issues = stale_issues + translated_issues
    if issues:
        for issue in issues[:120]:
            print(f" - {issue}", file=sys.stderr)
        if len(issues) > 120:
            print(f" - ... {len(issues) - 120} more", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
