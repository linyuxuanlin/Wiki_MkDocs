#!/usr/bin/env python3
"""Audit translation structure against zh source without changing content.

The checks are intentionally structural rather than linguistic: a translation
may use very different words and length, but it should not silently lose major
headings, fenced code blocks, images, or same-site references from the source.
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

SOURCE_DIR = Path("docs/zh")
LOCALE_DIRS = (Path("docs/en"), Path("docs/es"), Path("docs/ar"))

_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+", re.MULTILINE)
_FENCE_RE = re.compile(r"^\s*(?:```|~~~)", re.MULTILINE)
_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(")
_SAME_SITE_RE = re.compile(r"https?://(?:www\.)?wiki-power\.com/|\]\(/")
_FRONTMATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.DOTALL)
_FENCED_BLOCK_RE = re.compile(r"(^\s*(```|~~~).*?^\s*\2\s*$)", re.MULTILINE | re.DOTALL)
_URL_RE = re.compile(r"https?://\S+")
_MARKUP_RE = re.compile(r"[#>*_`|\[\](){}!~-]+")
_SPACE_RE = re.compile(r"\s+")


@dataclass(frozen=True)
class Metrics:
    visible_chars: int
    headings: int
    fence_lines: int
    images: int
    same_site_refs: int


def metrics(text: str) -> Metrics:
    body = _FRONTMATTER_RE.sub("", text, count=1)
    visible = _FENCED_BLOCK_RE.sub(" ", body)
    visible = _URL_RE.sub(" ", visible)
    visible = _MARKUP_RE.sub(" ", visible)
    visible = _SPACE_RE.sub("", visible)
    return Metrics(
        visible_chars=len(visible),
        headings=len(_HEADING_RE.findall(body)),
        fence_lines=len(_FENCE_RE.findall(body)),
        images=len(_IMAGE_RE.findall(body)),
        same_site_refs=len(_SAME_SITE_RE.findall(body)),
    )


def assess(source: Metrics, translated: Metrics) -> tuple[int, list[str]]:
    score = 0
    reasons: list[str] = []

    if source.visible_chars >= 800:
        ratio = translated.visible_chars / max(source.visible_chars, 1)
        if ratio < 0.35:
            score += 5
            reasons.append(f"very-short={ratio:.0%}")
        elif ratio < 0.50:
            score += 2
            reasons.append(f"short={ratio:.0%}")

    if source.headings >= 2 and translated.headings < source.headings:
        missing = source.headings - translated.headings
        score += 2 + min(missing, 3)
        reasons.append(f"headings={translated.headings}/{source.headings}")

    if translated.fence_lines != source.fence_lines:
        score += 4
        reasons.append(f"fences={translated.fence_lines}/{source.fence_lines}")

    if translated.images != source.images:
        score += 3
        reasons.append(f"images={translated.images}/{source.images}")

    if translated.same_site_refs < source.same_site_refs:
        missing = source.same_site_refs - translated.same_site_refs
        score += 2 + min(missing, 3)
        reasons.append(f"internal-refs={translated.same_site_refs}/{source.same_site_refs}")

    return score, reasons


def main() -> int:
    checked = 0
    candidates: list[tuple[int, str, Metrics, Metrics, list[str]]] = []
    locale_counts: Counter[str] = Counter()

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
            score, reasons = assess(source_metrics, translated_metrics)
            if score < 3:
                continue

            key = translated_path.as_posix()
            candidates.append(
                (score, key, source_metrics, translated_metrics, reasons)
            )
            locale_counts[locale_dir.name] += 1

    candidates.sort(key=lambda item: (-item[0], item[1]))

    print(f"Translated files checked: {checked}")
    print(f"High-confidence structural candidates: {len(candidates)}")
    print(
        "By locale: "
        + ", ".join(
            f"{locale}={locale_counts[locale]}" for locale in ("en", "es", "ar")
        )
    )

    print("\nCandidates:")
    if not candidates:
        print("    0  none")
    for score, path, source, translated, reasons in candidates[:120]:
        print(
            f"{score:2d}  {path}  "
            + ", ".join(reasons)
            + f"; chars={translated.visible_chars}/{source.visible_chars}"
        )

    if len(candidates) > 120:
        print(f"... {len(candidates) - 120} more")

    # Diagnostic only. A later change may turn a reviewed high-confidence list
    # into index/monetization quarantine rules, but this audit never guesses.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
