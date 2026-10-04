#!/usr/bin/env python3
"""Validate quarantine behavior for deterministically malformed translations."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

DOCS_DIR = Path("docs")
SITE_DIR = Path("site")
SITE_ORIGIN = "https://wiki-power.com"
LOCALES = ("en", "es", "ar")
_FRONTMATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.DOTALL)
_MARKDOWN_WRAPPER_RE = re.compile(r"^\s*(?:`{3,}|~{3,})\s*markdown\s*$", re.IGNORECASE)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.robots: str | None = None
        self.alternates: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        values = {key.lower(): value for key, value in attrs if key}
        tag = tag.lower()
        if tag == "meta" and (values.get("name") or "").lower() == "robots":
            self.robots = values.get("content")
            return
        if tag != "link":
            return
        rel = (values.get("rel") or "").lower().split()
        language = (values.get("hreflang") or "").lower()
        href = values.get("href")
        if "alternate" in rel and language and href:
            self.alternates.append((language, href))


def first_nonempty_line(text: str) -> str:
    text = _FRONTMATTER_RE.sub("", text, count=1)
    for line in text.splitlines():
        if line.strip():
            return line
    return ""


def starts_markdown_wrapper(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    return bool(_MARKDOWN_WRAPPER_RE.match(first_nonempty_line(text)))


def normalize_path(value: str) -> str:
    path = unquote(urlsplit(value).path) or "/"
    if not path.startswith("/"):
        path = "/" + path
    if path != "/" and not path.endswith("/"):
        path += "/"
    return path


def route_for_source(locale: str, relative_md: Path) -> str:
    relative = relative_md.with_suffix("").as_posix()
    return f"/{locale}/{relative}/"


def root_route_for_source(relative_md: Path) -> str:
    relative = relative_md.with_suffix("").as_posix()
    return f"/{relative}/"


def generated_index_for_route(route: str) -> Path:
    if route == "/":
        return SITE_DIR / "index.html"
    return SITE_DIR / route.strip("/") / "index.html"


def parse_page(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    return parser


def expected_quarantines() -> list[tuple[str, Path, str, str]]:
    results: list[tuple[str, Path, str, str]] = []
    zh_dir = DOCS_DIR / "zh"

    for locale in LOCALES:
        locale_dir = DOCS_DIR / locale
        if not locale_dir.is_dir():
            continue
        for translated in sorted(locale_dir.rglob("*.md")):
            relative = translated.relative_to(locale_dir)
            source = zh_dir / relative
            if not source.is_file():
                continue
            if not starts_markdown_wrapper(translated):
                continue
            if starts_markdown_wrapper(source):
                continue
            results.append(
                (
                    locale,
                    relative,
                    route_for_source(locale, relative),
                    root_route_for_source(relative),
                )
            )

    return results


def sitemap_signals(errors: list[str]) -> tuple[set[str], set[str]]:
    path = SITE_DIR / "sitemap.xml"
    try:
        root = ET.parse(path).getroot()
    except Exception as exc:
        errors.append(f"sitemap.xml is not valid XML: {exc}")
        return set(), set()

    ns = {
        "sm": "http://www.sitemaps.org/schemas/sitemap/0.9",
        "xhtml": "http://www.w3.org/1999/xhtml",
    }
    locations: set[str] = set()
    alternate_targets: set[str] = set()

    for url_node in root.findall("sm:url", ns):
        loc = url_node.find("sm:loc", ns)
        if loc is not None and loc.text:
            locations.add(normalize_path(loc.text))
        for link in url_node.findall("xhtml:link", ns):
            href = link.attrib.get("href")
            if href:
                alternate_targets.add(normalize_path(href))

    return locations, alternate_targets


def main() -> int:
    errors: list[str] = []

    if not SITE_DIR.is_dir():
        print("site/ is missing; run `mkdocs build --clean` first.", file=sys.stderr)
        return 2

    quarantines = expected_quarantines()
    if not quarantines:
        print(
            "Translation quarantine validation found no deterministic malformed translations; "
            "the quarantine path is not being exercised.",
            file=sys.stderr,
        )
        return 2

    counts = Counter(locale for locale, _relative, _route, _root in quarantines)
    locations, sitemap_alternates = sitemap_signals(errors)
    quarantined_routes = {route for _locale, _relative, route, _root in quarantines}

    # Every deterministically malformed translation stays reachable, but must no
    # longer be advertised as an indexable/alternate localization target.
    for locale, relative, route, root_route in quarantines:
        output = generated_index_for_route(route)
        if not output.is_file():
            errors.append(f"{route}: quarantined translation output is missing")
            continue

        page = parse_page(output)
        robots = (page.robots or "").lower()
        if "noindex" not in robots:
            errors.append(f"{route}: quarantined translation is missing robots noindex")

        if route in locations:
            errors.append(f"{route}: quarantined translation is still a sitemap <loc>")
        if route in sitemap_alternates:
            errors.append(f"{route}: quarantined translation is still a sitemap hreflang target")

        root_output = generated_index_for_route(root_route)
        if not root_output.is_file():
            errors.append(f"{route}: corresponding root source output is missing: {root_route}")
            continue

        root_page = parse_page(root_output)
        root_robots = (root_page.robots or "").lower()
        if "noindex" in root_robots:
            errors.append(
                f"{root_route}: valid root source was accidentally quarantined with {route}"
            )

        advertised = {
            normalize_path(urljoin(SITE_ORIGIN + root_route, href))
            for _language, href in root_page.alternates
        }
        if route in advertised:
            errors.append(f"{root_route}: still advertises malformed {locale} alternate {route}")

    # Stronger global assertion: no generated page may advertise any quarantined
    # route through HTML hreflang, not just the corresponding root page.
    html_hreflang_refs = 0
    for html_path in sorted(SITE_DIR.rglob("index.html")):
        rel = html_path.relative_to(SITE_DIR).parent.as_posix()
        page_route = "/" if rel == "." else f"/{rel}/"
        page = parse_page(html_path)
        for language, href in page.alternates:
            html_hreflang_refs += 1
            target = normalize_path(urljoin(SITE_ORIGIN + page_route, href))
            if target in quarantined_routes:
                errors.append(
                    f"{page_route}: hreflang={language} advertises quarantined target {target}"
                )

    # The detector is intentionally narrow. A zh source that itself begins with
    # a Markdown wrapper is never considered a translation-quality quarantine.
    for zh_source in sorted((DOCS_DIR / "zh").rglob("*.md")):
        if not starts_markdown_wrapper(zh_source):
            continue
        root_route = root_route_for_source(zh_source.relative_to(DOCS_DIR / "zh"))
        output = generated_index_for_route(root_route)
        if not output.is_file():
            continue
        page = parse_page(output)
        if "noindex" in (page.robots or "").lower():
            errors.append(
                f"{root_route}: zh source with intentional wrapper was incorrectly noindexed"
            )

    if errors:
        print(
            f"Translation quarantine validation FAILED with {len(errors)} issue(s):",
            file=sys.stderr,
        )
        for error in errors[:100]:
            print(f" - {error}", file=sys.stderr)
        if len(errors) > 100:
            print(f" - ... {len(errors) - 100} more", file=sys.stderr)
        return 1

    print(
        "Translation quarantine validation passed: "
        f"{len(quarantines)} malformed translations quarantined "
        f"(en={counts['en']}, es={counts['es']}, ar={counts['ar']}); "
        f"{html_hreflang_refs} generated HTML hreflang links scanned; "
        "all quarantined pages remain reachable, noindexed, and absent from sitemap/hreflang signals."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
