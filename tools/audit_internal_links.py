#!/usr/bin/env python3
"""Report internal links that point to generated noncanonical fallback pages."""

from __future__ import annotations

from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

SITE_DIR = Path("site")
ORIGIN = "https://wiki-power.com"


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.canonical: str | None = None
        self.links: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        values = {key.lower(): value for key, value in attrs if key}
        tag = tag.lower()
        if tag == "link":
            rel = (values.get("rel") or "").lower().split()
            if "canonical" in rel and values.get("href"):
                self.canonical = values["href"]
        elif tag == "a" and values.get("href"):
            self.links.append((values["href"], values.get("class") or ""))


def normalize(value: str) -> str:
    path = unquote(urlsplit(value).path)
    if not path:
        return "/"
    if not path.startswith("/"):
        path = "/" + path
    if path.endswith("/index.html"):
        path = path[: -len("index.html")]
    if path != "/" and not path.endswith("/") and "." not in Path(path).name:
        path += "/"
    return path


def route_for(path: Path) -> str:
    rel = path.relative_to(SITE_DIR)
    if rel.name == "404.html":
        return "/404.html"
    parent = rel.parent.as_posix()
    return "/" if parent == "." else f"/{parent}/"


def main() -> int:
    html_files = sorted(SITE_DIR.rglob("*.html"))
    pages: dict[str, tuple[str, list[tuple[str, str]]]] = {}

    for path in html_files:
        route = route_for(path)
        html = path.read_text(encoding="utf-8", errors="replace")
        parser = LinkParser()
        parser.feed(html)
        canonical = route
        if parser.canonical:
            canonical = normalize(urljoin(ORIGIN + route, parser.canonical))
        pages[route] = (canonical, parser.links)

    noncanonical_targets = {
        route: canonical
        for route, (canonical, _links) in pages.items()
        if route != canonical and route != "/404.html"
    }

    target_counts: Counter[str] = Counter()
    target_nav_counts: Counter[str] = Counter()
    source_counts: Counter[str] = Counter()
    examples: dict[str, list[str]] = defaultdict(list)

    total_internal = 0
    noncanonical_internal = 0

    for source_route, (_canonical, links) in pages.items():
        for href, classes in links:
            absolute = urljoin(ORIGIN + source_route, href)
            parts = urlsplit(absolute)
            if parts.netloc != "wiki-power.com":
                continue
            target = normalize(absolute)
            if target not in pages:
                continue
            total_internal += 1
            if target not in noncanonical_targets:
                continue

            noncanonical_internal += 1
            target_counts[target] += 1
            source_counts[source_route] += 1
            if "md-nav__link" in classes or "md-tabs__link" in classes or "md-select__link" in classes:
                target_nav_counts[target] += 1
            if len(examples[target]) < 3:
                examples[target].append(source_route)

    print(f"Generated HTML files: {len(html_files)}")
    print(f"Generated noncanonical page targets: {len(noncanonical_targets)}")
    print(f"Internal links to generated pages: {total_internal}")
    print(f"Internal links to noncanonical pages: {noncanonical_internal}")
    if total_internal:
        print(f"Share: {noncanonical_internal / total_internal:.2%}")

    print("\nTop noncanonical targets:")
    for target, count in target_counts.most_common(40):
        canonical = noncanonical_targets[target]
        nav_count = target_nav_counts[target]
        sample = ", ".join(examples[target])
        print(
            f"{count:5d} links ({nav_count:5d} nav)  {target} -> {canonical}"
            f"  sources: {sample}"
        )

    print("\nTop source pages linking to noncanonical targets:")
    for source, count in source_counts.most_common(20):
        print(f"{count:5d}  {source}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
