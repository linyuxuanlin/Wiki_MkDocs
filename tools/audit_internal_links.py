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
        self.article_depth = 0
        self.nav_depth = 0
        self.footer_depth = 0

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

        if tag == "link":
            rel = (values.get("rel") or "").lower().split()
            if "canonical" in rel and values.get("href"):
                self.canonical = values["href"]
        elif tag == "a" and values.get("href"):
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
    target_context_counts: dict[str, Counter[str]] = defaultdict(Counter)
    source_counts: Counter[str] = Counter()
    examples: dict[str, list[str]] = defaultdict(list)

    actionable_target_counts: Counter[str] = Counter()
    actionable_source_counts: Counter[str] = Counter()
    actionable_examples: dict[str, list[str]] = defaultdict(list)

    total_internal = 0
    noncanonical_internal = 0
    context_counts: Counter[str] = Counter()
    canonical_article_noncanonical = 0
    fallback_article_noncanonical = 0

    for source_route, (source_canonical, links) in pages.items():
        source_is_canonical = source_route == source_canonical

        for href, context in links:
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
            context_counts[context] += 1
            target_counts[target] += 1
            target_context_counts[target][context] += 1
            source_counts[source_route] += 1
            if len(examples[target]) < 3:
                examples[target].append(source_route)

            if context == "article":
                if source_is_canonical:
                    canonical_article_noncanonical += 1
                    actionable_target_counts[target] += 1
                    actionable_source_counts[source_route] += 1
                    if len(actionable_examples[target]) < 3:
                        actionable_examples[target].append(source_route)
                else:
                    fallback_article_noncanonical += 1

    print(f"Generated HTML files: {len(html_files)}")
    print(f"Generated noncanonical page targets: {len(noncanonical_targets)}")
    print(f"Internal links to generated pages: {total_internal}")
    print(f"Internal links to noncanonical pages: {noncanonical_internal}")
    if total_internal:
        print(f"Share: {noncanonical_internal / total_internal:.2%}")
    print(
        "Noncanonical link contexts: "
        + ", ".join(
            f"{name}={context_counts[name]}"
            for name in ("nav", "article", "footer", "other")
        )
    )
    print(
        "Article links to noncanonical pages: "
        f"canonical-source={canonical_article_noncanonical}, "
        f"fallback-source={fallback_article_noncanonical}"
    )

    print("\nTop noncanonical targets (all contexts):")
    for target, count in target_counts.most_common(30):
        canonical = noncanonical_targets[target]
        contexts = target_context_counts[target]
        sample = ", ".join(examples[target])
        print(
            f"{count:5d} links "
            f"(nav={contexts['nav']}, article={contexts['article']}, "
            f"footer={contexts['footer']}, other={contexts['other']})  "
            f"{target} -> {canonical}  sources: {sample}"
        )

    print("\nTop actionable targets from canonical article content:")
    if not actionable_target_counts:
        print("    0  none")
    for target, count in actionable_target_counts.most_common(40):
        canonical = noncanonical_targets[target]
        sample = ", ".join(actionable_examples[target])
        print(f"{count:5d}  {target} -> {canonical}  sources: {sample}")

    print("\nTop canonical source pages with actionable article links:")
    if not actionable_source_counts:
        print("    0  none")
    for source, count in actionable_source_counts.most_common(40):
        print(f"{count:5d}  {source}")

    print("\nTop source pages linking to noncanonical targets (all contexts):")
    for source, count in source_counts.most_common(20):
        print(f"{count:5d}  {source}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
