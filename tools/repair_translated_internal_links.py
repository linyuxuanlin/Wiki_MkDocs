#!/usr/bin/env python3
"""Restore same-site Markdown link destinations in translations from zh originals.

Machine translation is allowed to translate visible link labels, but it must not
translate wiki-power.com URL paths. This postprocessor aligns internal link
destinations by source order while leaving all translated prose untouched.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit

SOURCE_DIR = Path("docs/zh")
LOCALE_DIRS = (Path("docs/en"), Path("docs/es"), Path("docs/ar"))
SITE_HOSTS = {"wiki-power.com", "www.wiki-power.com"}


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
                    value = text[start:index]
                    results.append(Destination(start, index, value))
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

    if not replacements:
        return translated, 0, None

    output = translated
    for start, end, value in reversed(replacements):
        output = output[:start] + value + output[end:]
    return output, len(replacements), None


def process(check_only: bool) -> tuple[int, int, list[str]]:
    files_checked = 0
    destinations_changed = 0
    issues: list[str] = []

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
                issues.append(f"{translated_path}: {issue}")
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

    return files_checked, destinations_changed, issues


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

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="report translated internal destinations that differ instead of repairing them",
    )
    args = parser.parse_args()

    test_errors = synthetic_tests()
    if test_errors:
        for error in test_errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 2

    files_checked, changed, issues = process(args.check)
    mode = "check" if args.check else "repair"
    print(
        f"Translation link {mode}: checked {files_checked} translated files; "
        f"{changed} internal destination(s) {'would change' if args.check else 'repaired'}."
    )

    if issues:
        for issue in issues[:120]:
            print(f" - {issue}", file=sys.stderr)
        if len(issues) > 120:
            print(f" - ... {len(issues) - 120} more", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
