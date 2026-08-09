#!/usr/bin/env python3
"""Audit generated same-site hyperlinks that do not resolve to generated output."""

from __future__ import annotations

from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

SITE_DIR = Path("site")
ORIGIN = "https://wiki-power.com"
IGNORED_SCHEMES = {"mailto", "tel", "javascript", "data"}


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.article_depth = 0
        self.nav_depth = 0
        self.footer_depth = 0
        self.links: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        values = {key.lower(): value for key, value in attrs if key}
        tag = tag.lower()

        if tag == "article":
            classes = (values.get("class") or "").split()
            if "md-content__inner" in classes:
                self.article_depth += 1
        elif tag == "nav":
            self.nav_depth += 1
        elif tag == "footer":
            self.footer_depth += 1

        if tag != "a" or not values.get("href"):
            return

        if self.article_depth:
            context = "article"
        elif self.nav_depth:
            context = "nav"
        elif self.footer_depth:
            context = "footer"
        else:
            context = "other"
        self.links.append((values["href"], context))

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "article" and self.article_depth:
            self.article_depth -= 1
        elif tag == "nav" and self.nav_depth:
            self.nav_depth -= 1
        elif tag == "footer" and self.footer_depth:
            self.footer_depth -= 1


def route_for(path: Path) -> str:
    rel = path.relative_to(SITE_DIR)
    if rel.name == "404.html":
        return "/404.html"
    parent = rel.parent.as_posix()
    return "/" if parent == "." else f"/{parent}/"


def normalized_path(value: str) -> str:
    path = unquote(urlsplit(value).path) or "/"
    if not path.startswith("/"):
        path = "/" + path
    return path


def generated_targets() -> set[str]:
    targets: set[str] = {"/"}
    for path in SITE_DIR.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(SITE_DIR).as_posix()
        file_url = "/" + unquote(rel)
        targets.add(file_url)

        if path.name == "index.html":
            parent = path.relative_to(SITE_DIR).parent.as_posix()
            route = "/" if parent == "." else f"/{unquote(parent)}/"
            targets.add(route)
            if route != "/":
                targets.add(route.rstrip("/"))
    return targets


def main() -> int:
    html_files = sorted(SITE_DIR.rglob("*.html"))
    targets = generated_targets()

    broken_counts: Counter[str] = Counter()
    context_counts: Counter[str] = Counter()
    source_counts: Counter[str] = Counter()
    examples: dict[str, list[str]] = defaultdict(list)
    checked = 0

    for path in html_files:
        source_route = route_for(path)
        html = path.read_text(encoding="utf-8", errors="replace")
        parser = LinkParser()
        parser.feed(html)

        for href, context in parser.links:
            raw_parts = urlsplit(href)
            if raw_parts.scheme.lower() in IGNORED_SCHEMES:
                continue

            absolute = urljoin(ORIGIN + source_route, href)
            parts = urlsplit(absolute)
            if parts.netloc.lower() != "wiki-power.com":
                continue

            checked += 1
            target = normalized_path(absolute)
            if target in targets:
                continue

            broken_counts[target] += 1
            context_counts[context] += 1
            source_counts[source_route] += 1
            if len(examples[target]) < 4:
                examples[target].append(source_route)

    total_broken = sum(broken_counts.values())
    print(f"Generated HTML files: {len(html_files)}")
    print(f"Generated URL/file targets: {len(targets)}")
    print(f"Same-site hyperlinks checked: {checked}")
    print(f"Unresolved same-site hyperlink occurrences: {total_broken}")
    print(f"Unique unresolved targets: {len(broken_counts)}")
    print(
        "Unresolved contexts: "
        + ", ".join(
            f"{name}={context_counts[name]}"
            for name in ("nav", "article", "footer", "other")
        )
    )

    print("\nTop unresolved targets:")
    if not broken_counts:
        print("    0  none")
    for target, count in broken_counts.most_common(80):
        sample = ", ".join(examples[target])
        print(f"{count:5d}  {target}  sources: {sample}")

    print("\nTop source pages with unresolved same-site links:")
    if not source_counts:
        print("    0  none")
    for source, count in source_counts.most_common(40):
        print(f"{count:5d}  {source}")

    # Diagnostic only. Review the report before deciding whether any links need edits.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
