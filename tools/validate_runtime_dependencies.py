#!/usr/bin/env python3
"""Validate critical runtime dependency placement in generated HTML."""

from __future__ import annotations

import sys
from pathlib import Path

SITE_DIR = Path("site")
PANGU_CDN = "cdnjs.cloudflare.com/ajax/libs/pangu/"
PANGU_LOCAL = "javascripts/pangu.min.js"


def main() -> int:
    errors: list[str] = []

    if not SITE_DIR.is_dir():
        print("site/ is missing; run `mkdocs build --clean` first.", file=sys.stderr)
        return 2

    local_file = SITE_DIR / PANGU_LOCAL
    if not local_file.is_file():
        errors.append(f"missing vendored runtime: {PANGU_LOCAL}")
    else:
        text = local_file.read_text(encoding="utf-8", errors="replace")
        if "@version: 4.0.7" not in text:
            errors.append("vendored Pangu version is not the expected 4.0.7")

    html_files = sorted(SITE_DIR.rglob("*.html"))
    if not html_files:
        errors.append("no generated HTML files found")

    local_refs = 0
    for path in html_files:
        html = path.read_text(encoding="utf-8", errors="replace")
        rel = path.relative_to(SITE_DIR)
        if PANGU_CDN in html:
            errors.append(f"{rel}: still references the external Pangu CDN")
        if PANGU_LOCAL in html:
            local_refs += 1
        else:
            errors.append(f"{rel}: missing local Pangu runtime reference")

    if errors:
        print(f"Runtime dependency validation FAILED with {len(errors)} issue(s):", file=sys.stderr)
        for error in errors[:80]:
            print(f" - {error}", file=sys.stderr)
        if len(errors) > 80:
            print(f" - ... {len(errors) - 80} more", file=sys.stderr)
        return 1

    print(
        "Runtime dependency validation passed: "
        f"{len(html_files)} HTML files use vendored Pangu; zero CDN references."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
