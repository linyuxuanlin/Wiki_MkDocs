#!/usr/bin/env python3
"""Repair exact malformed Markdown destinations that strict URL parsing must reject.

This pre-pass is intentionally tiny and exact-match only. It exists for legacy
machine translations where a model inserted literal spaces into a wiki-power.com
URL path. We do not loosen the general link parser because whitespace can also
introduce a valid Markdown link title, e.g. `(url "title")`.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

DOCS_DIR = Path("docs")

EXACT_DESTINATION_REPLACEMENTS = {
    "https://wiki-power.com/PlatformIO—una herramienta de desarrollo embebido todo en uno":
        "https://wiki-power.com/PlatformIO—一站式嵌入式开发工具/",
}


@dataclass(frozen=True)
class Destination:
    start: int
    end: int
    value: str


def markdown_destinations(text: str) -> list[Destination]:
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


def repair_text(text: str) -> tuple[str, int]:
    replacements: list[tuple[int, int, str]] = []
    for item in markdown_destinations(text):
        replacement = EXACT_DESTINATION_REPLACEMENTS.get(item.value.strip())
        if replacement and replacement != item.value:
            replacements.append((item.start, item.end, replacement))

    output = text
    for start, end, value in reversed(replacements):
        output = output[:start] + value + output[end:]
    return output, len(replacements)


def synthetic_tests() -> list[str]:
    errors: list[str] = []
    bad = next(iter(EXACT_DESTINATION_REPLACEMENTS))
    good = EXACT_DESTINATION_REPLACEMENTS[bad]

    source = f"[Previous]({bad})"
    repaired, changed = repair_text(source)
    if changed != 1 or good not in repaired:
        errors.append("exact malformed destination was not repaired")

    titled = f'[Previous]({bad} "title")'
    titled_repaired, titled_changed = repair_text(titled)
    if titled_changed != 0 or titled_repaired != titled:
        errors.append("destination with Markdown title was unexpectedly changed")

    plain = f"Plain text URL: {bad}"
    plain_repaired, plain_changed = repair_text(plain)
    if plain_changed != 0 or plain_repaired != plain:
        errors.append("plain prose was unexpectedly changed")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="report exact malformed destinations that remain instead of writing them",
    )
    args = parser.parse_args()

    errors = synthetic_tests()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 2

    files_checked = 0
    changed_destinations = 0
    issues: list[str] = []

    for path in sorted(DOCS_DIR.rglob("*.md")):
        files_checked += 1
        text = path.read_text(encoding="utf-8")
        repaired, changed = repair_text(text)
        if not changed:
            continue

        changed_destinations += changed
        if args.check:
            issues.append(f"{path}: {changed} malformed exact destination(s)")
        else:
            path.write_text(repaired, encoding="utf-8")

    mode = "check" if args.check else "repair"
    print(
        f"Malformed internal URL {mode}: checked {files_checked} Markdown files; "
        f"{changed_destinations} destination(s) "
        f"{'would change' if args.check else 'repaired'}."
    )

    if issues:
        for issue in issues:
            print(f" - {issue}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
