#!/usr/bin/env python3
"""Conservatively audit translated Markdown for likely structural loss.

This is intentionally a *loss* detector, not a translation-quality scorer. A
translation may be longer, use different wording, or even contain extra code
blocks. We only flag pages that appear to have dropped substantial source
structure, an extreme amount of visible content, or a deterministic malformed
whole-document Markdown wrapper introduced by machine translation.
"""

from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

SOURCE_DIR = Path("docs/zh")
LOCALE_DIRS = (Path("docs/en"), Path("docs/es"), Path("docs/ar"))

_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+", re.MULTILINE)
_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(")
_SAME_SITE_RE = re.compile(r"https?://(?:www\.)?wiki-power\.com/|\]\(/")
_FRONTMATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.DOTALL)
_URL_RE = re.compile(r"https?://\S+")
_MARKUP_RE = re.compile(r"[#>*_`|\[\](){}!~-]+")
_SPACE_RE = re.compile(r"\s+")
_MARKDOWN_WRAPPER_RE = re.compile(r"^\s*(`{3,}|~{3,})\s*markdown\s*$", re.IGNORECASE)


@dataclass(frozen=True)
class Metrics:
    visible_chars: int
    headings: int
    fenced_blocks: int
    images: int
    same_site_refs: int
    starts_markdown_wrapper: bool


def first_nonempty_line(text: str) -> str:
    body = _FRONTMATTER_RE.sub("", text, count=1)
    for line in body.splitlines():
        if line.strip():
            return line
    return ""


def count_complete_fenced_blocks(text: str) -> int:
    """Count complete Markdown fenced code blocks, ignoring unmatched extras."""
    blocks = 0
    opening_char: str | None = None
    opening_length = 0

    for line in text.splitlines():
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        if indent > 3 or not stripped:
            continue

        marker_char = stripped[0]
        if marker_char not in {"`", "~"}:
            continue

        marker_length = 0
        while marker_length < len(stripped) and stripped[marker_length] == marker_char:
            marker_length += 1
        if marker_length < 3:
            continue

        if opening_char is None:
            opening_char = marker_char
            opening_length = marker_length
            continue

        if marker_char != opening_char or marker_length < opening_length:
            continue
        if stripped[marker_length:].strip():
            continue

        blocks += 1
        opening_char = None
        opening_length = 0

    return blocks


def strip_fenced_blocks(text: str) -> str:
    """Remove complete fenced blocks when estimating prose/content length."""
    output: list[str] = []
    in_fence = False
    opening_char: str | None = None
    opening_length = 0

    for line in text.splitlines():
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        marker_char = stripped[0] if stripped and indent <= 3 else ""
        marker_length = 0
        if marker_char in {"`", "~"}:
            while marker_length < len(stripped) and stripped[marker_length] == marker_char:
                marker_length += 1

        if not in_fence and marker_length >= 3:
            in_fence = True
            opening_char = marker_char
            opening_length = marker_length
            continue

        if in_fence:
            if (
                marker_char == opening_char
                and marker_length >= opening_length
                and not stripped[marker_length:].strip()
            ):
                in_fence = False
                opening_char = None
                opening_length = 0
            continue

        output.append(line)

    return "\n".join(output)


def metrics(text: str) -> Metrics:
    body = _FRONTMATTER_RE.sub("", text, count=1)
    visible = strip_fenced_blocks(body)
    visible = _URL_RE.sub(" ", visible)
    visible = _MARKUP_RE.sub(" ", visible)
    visible = _SPACE_RE.sub("", visible)
    return Metrics(
        visible_chars=len(visible),
        headings=len(_HEADING_RE.findall(body)),
        fenced_blocks=count_complete_fenced_blocks(body),
        images=len(_IMAGE_RE.findall(body)),
        same_site_refs=len(_SAME_SITE_RE.findall(body)),
        starts_markdown_wrapper=bool(_MARKDOWN_WRAPPER_RE.match(first_nonempty_line(body))),
    )


def significant_deficit(source_count: int, translated_count: int, *, min_source: int) -> bool:
    if source_count < min_source or translated_count >= source_count:
        return False
    missing = source_count - translated_count
    threshold = max(1, math.ceil(source_count * 0.25))
    return missing >= threshold


def assess(source: Metrics, translated: Metrics) -> tuple[bool, int, list[str]]:
    """Return (severe, independent_loss_signal_count, reasons)."""
    reasons: list[str] = []
    loss_signals = 0
    deterministic_corruption = False
    extreme_length_loss = False

    if translated.starts_markdown_wrapper and not source.starts_markdown_wrapper:
        deterministic_corruption = True
        loss_signals += 1
        reasons.append("malformed-markdown-wrapper")

    if source.visible_chars >= 500:
        ratio = translated.visible_chars / max(source.visible_chars, 1)
        if ratio < 0.20:
            extreme_length_loss = True
            loss_signals += 1
            reasons.append(f"extreme-length={ratio:.0%}")
        elif ratio < 0.40:
            loss_signals += 1
            reasons.append(f"length={ratio:.0%}")

    if significant_deficit(source.headings, translated.headings, min_source=4):
        loss_signals += 1
        reasons.append(f"headings={translated.headings}/{source.headings}")

    # Only missing complete code blocks matter. Extra translated fences are not
    # evidence of loss and previously created many false positives.
    if source.fenced_blocks and translated.fenced_blocks < source.fenced_blocks:
        loss_signals += 1
        reasons.append(f"code-blocks={translated.fenced_blocks}/{source.fenced_blocks}")

    if significant_deficit(source.images, translated.images, min_source=2):
        loss_signals += 1
        reasons.append(f"images={translated.images}/{source.images}")

    if significant_deficit(source.same_site_refs, translated.same_site_refs, min_source=2):
        loss_signals += 1
        reasons.append(
            f"internal-refs={translated.same_site_refs}/{source.same_site_refs}"
        )

    # A machine-added whole-document Markdown wrapper is deterministic output
    # corruption and is sufficient by itself. Otherwise require either dramatic
    # truncation or at least two independent kinds of structural loss.
    severe = deterministic_corruption or extreme_length_loss or loss_signals >= 2
    return severe, loss_signals, reasons


def main() -> int:
    checked = 0
    candidates: list[tuple[int, str, Metrics, Metrics, list[str]]] = []
    locale_counts: Counter[str] = Counter()
    wrapper_counts: Counter[str] = Counter()

    for source_path in sorted(SOURCE_DIR.glob("*.md")):
        source_text = source_path.read_text(encoding="utf-8")
        source_metrics = metrics(source_text)

        for locale_dir in LOCALE_DIRS:
            translated_path = locale_dir / source_path.name
            if not translated_path.is_file():
                continue

            checked += 1
            translated_text = translated_path.read_text(encoding="utf-8")
            translated_metrics = metrics(translated_text)
            severe, loss_signals, reasons = assess(source_metrics, translated_metrics)
            if not severe:
                continue

            key = translated_path.as_posix()
            candidates.append(
                (loss_signals, key, source_metrics, translated_metrics, reasons)
            )
            locale_counts[locale_dir.name] += 1
            if "malformed-markdown-wrapper" in reasons:
                wrapper_counts[locale_dir.name] += 1

    candidates.sort(
        key=lambda item: (
            "malformed-markdown-wrapper" not in item[4],
            -item[0],
            item[3].visible_chars / max(item[2].visible_chars, 1),
            item[1],
        )
    )

    print(f"Translated files checked: {checked}")
    print(f"Conservative severe structural candidates: {len(candidates)}")
    print(
        "By locale: "
        + ", ".join(
            f"{locale}={locale_counts[locale]}" for locale in ("en", "es", "ar")
        )
    )
    print(
        "Deterministic malformed Markdown wrappers: "
        + ", ".join(
            f"{locale}={wrapper_counts[locale]}" for locale in ("en", "es", "ar")
        )
    )

    print("\nCandidates:")
    if not candidates:
        print("    0  none")
    for signals, path, source, translated, reasons in candidates[:120]:
        print(
            f"{signals:2d} signals  {path}  "
            + ", ".join(reasons)
            + (
                f"; chars={translated.visible_chars}/{source.visible_chars}; "
                f"blocks={translated.fenced_blocks}/{source.fenced_blocks}"
            )
        )

    if len(candidates) > 120:
        print(f"... {len(candidates) - 120} more")

    # Diagnostic only. Every eventual quarantine entry must still be reviewed;
    # this audit deliberately does not modify indexing or content.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
