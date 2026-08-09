#!/usr/bin/env python3
"""Adversarial assertions against the fully generated MkDocs site."""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

SITE_DIR = Path("site")
SITE_ORIGIN = "https://wiki-power.com"
DEFAULT_DESCRIPTION = "博览万物，融会贯通。"


@dataclass
class PageSignals:
    route: str
    path: Path
    html_lang: str | None = None
    canonical: str | None = None
    description: str | None = None
    robots: str | None = None
    alternates: list[tuple[str, str]] = field(default_factory=list)
    html: str = ""


class SignalParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.html_lang = None
        self.canonical = None
        self.description = None
        self.robots = None
        self.alternates = []

    def handle_starttag(self, tag: str, attrs) -> None:
        values = {key.lower(): value for key, value in attrs if key}
        tag = tag.lower()

        if tag == "html" and self.html_lang is None:
            self.html_lang = values.get("lang")
            return

        if tag == "meta":
            name = (values.get("name") or "").lower()
            if name == "description":
                self.description = values.get("content")
            elif name == "robots":
                self.robots = values.get("content")
            return

        if tag != "link":
            return

        rel = (values.get("rel") or "").lower().split()
        if "canonical" in rel:
            self.canonical = values.get("href")

        hreflang = values.get("hreflang")
        href = values.get("href")
        if "alternate" in rel and hreflang and href:
            self.alternates.append((hreflang.lower(), href))


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def normalize_path(value: str) -> str:
    path = unquote(urlsplit(value).path)
    if not path:
        return "/"
    if not path.startswith("/"):
        path = "/" + path
    if path != "/" and not path.endswith("/"):
        path += "/"
    return path


def route_for(path: Path) -> str:
    rel = path.relative_to(SITE_DIR)
    parent = rel.parent.as_posix()
    return "/" if parent == "." else f"/{parent}/"


def parse_page(path: Path) -> PageSignals:
    html = path.read_text(encoding="utf-8")
    parser = SignalParser()
    parser.feed(html)
    return PageSignals(
        route=route_for(path),
        path=path,
        html_lang=parser.html_lang,
        canonical=parser.canonical,
        description=parser.description,
        robots=parser.robots,
        alternates=parser.alternates,
        html=html,
    )


def sitemap_paths(errors: list[str]) -> set[str]:
    path = SITE_DIR / "sitemap.xml"
    try:
        root = ET.parse(path).getroot()
    except Exception as exc:
        fail(errors, f"sitemap.xml is not valid XML: {exc}")
        return set()

    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    values = set()
    for node in root.findall("sm:url/sm:loc", ns):
        if node.text:
            values.add(normalize_path(node.text))
    if not values:
        fail(errors, "sitemap.xml contains no <loc> entries")
    return values


def validate_rss(errors: list[str], name: str) -> None:
    path = SITE_DIR / name
    try:
        root = ET.parse(path).getroot()
    except Exception as exc:
        fail(errors, f"{name} is not valid XML: {exc}")
        return

    channel = root.find("channel")
    if channel is None:
        fail(errors, f"{name} has no RSS channel")
        return

    language = (channel.findtext("language") or "").strip()
    description = (channel.findtext("description") or "").strip()
    if language != "zh":
        fail(errors, f"{name} language leaked from another locale: {language!r}")
    if description != DEFAULT_DESCRIPTION:
        fail(errors, f"{name} description leaked/changed unexpectedly: {description!r}")

    guids = [
        (item.findtext("guid") or "").strip()
        for item in channel.findall("item")
        if (item.findtext("guid") or "").strip()
    ]
    if len(guids) != len(set(guids)):
        fail(errors, f"{name} contains duplicate item GUIDs after multilingual builds")


def main() -> int:
    errors: list[str] = []

    if not SITE_DIR.is_dir():
        print("site/ is missing; run `mkdocs build --clean` first.", file=sys.stderr)
        return 2

    page_paths = sorted(SITE_DIR.rglob("index.html"))
    if not page_paths:
        print("No generated HTML pages found.", file=sys.stderr)
        return 2

    pages = {page.route: page for page in map(parse_page, page_paths)}
    sitemap = sitemap_paths(errors)

    noncanonical = 0
    hreflang_links = 0

    for route, page in pages.items():
        if not page.canonical:
            fail(errors, f"{route}: missing canonical URL")
            continue

        canonical_url = urljoin(SITE_ORIGIN + route, page.canonical)
        canonical_parts = urlsplit(canonical_url)
        if canonical_parts.netloc != "wiki-power.com":
            fail(errors, f"{route}: canonical points off-site: {canonical_url}")
            continue

        canonical_route = normalize_path(canonical_url)
        if canonical_route != route:
            noncanonical += 1
            if route in sitemap:
                fail(errors, f"{route}: noncanonical fallback is still in sitemap")

        canonical_target = pages.get(canonical_route)
        if canonical_target is None:
            fail(errors, f"{route}: canonical target is missing from generated site: {canonical_route}")
        elif canonical_target.canonical:
            target_canonical = normalize_path(
                urljoin(SITE_ORIGIN + canonical_route, canonical_target.canonical)
            )
            if target_canonical != canonical_route:
                fail(
                    errors,
                    f"{route}: canonical chain detected via {canonical_route} -> {target_canonical}",
                )

        seen_languages: set[str] = set()
        self_hreflang = None
        for language, href in page.alternates:
            hreflang_links += 1
            if language in seen_languages:
                fail(errors, f"{route}: duplicate hreflang={language}")
            seen_languages.add(language)

            alternate_url = urljoin(SITE_ORIGIN + route, href)
            alternate_parts = urlsplit(alternate_url)
            if alternate_parts.netloc != "wiki-power.com":
                fail(errors, f"{route}: hreflang {language} points off-site: {alternate_url}")
                continue

            alternate_route = normalize_path(alternate_url)
            target = pages.get(alternate_route)
            if target is None:
                fail(
                    errors,
                    f"{route}: hreflang {language} target is missing: {alternate_route}",
                )
                continue

            if not target.canonical:
                fail(errors, f"{route}: hreflang target has no canonical: {alternate_route}")
            else:
                target_canonical = normalize_path(
                    urljoin(SITE_ORIGIN + alternate_route, target.canonical)
                )
                if target_canonical != alternate_route:
                    fail(
                        errors,
                        f"{route}: hreflang {language} points to noncanonical fallback "
                        f"{alternate_route} -> {target_canonical}",
                    )

            if alternate_route == route:
                self_hreflang = language

        if canonical_route == route and self_hreflang and page.html_lang:
            if self_hreflang != page.html_lang.lower():
                fail(
                    errors,
                    f"{route}: html lang={page.html_lang!r} disagrees with "
                    f"self hreflang={self_hreflang!r}",
                )

        if page.description and "{ loading=lazy }" in page.description:
            fail(errors, f"{route}: meta description contains Markdown attribute debris")

    continuity = pages.get("/Continuity_Test/")
    if continuity is None:
        fail(errors, "/Continuity_Test/: missing from generated site")
    else:
        if (continuity.html_lang or "").lower() != "en":
            fail(errors, f"/Continuity_Test/: expected html lang=en, got {continuity.html_lang!r}")
        continuity_alts = {
            lang: normalize_path(urljoin(SITE_ORIGIN + continuity.route, href))
            for lang, href in continuity.alternates
        }
        if continuity_alts.get("en") != "/Continuity_Test/":
            fail(errors, "/Continuity_Test/: English hreflang must point to canonical root URL")
        if "/en/Continuity_Test/" in continuity_alts.values():
            fail(errors, "/Continuity_Test/: generated /en fallback is advertised via hreflang")

    fallback = pages.get("/en/Continuity_Test/")
    if fallback is None:
        fail(errors, "/en/Continuity_Test/: expected accessible fallback URL is missing")
    elif not fallback.canonical or normalize_path(
        urljoin(SITE_ORIGIN + fallback.route, fallback.canonical)
    ) != "/Continuity_Test/":
        fail(errors, "/en/Continuity_Test/: fallback canonical is not the root source URL")

    legacy = pages.get("/archive/nps/")
    if legacy is not None:
        for language, href in legacy.alternates:
            alternate_route = normalize_path(urljoin(SITE_ORIGIN + legacy.route, href))
            if alternate_route.startswith(("/en/archive/nps/", "/es/archive/nps/", "/ar/archive/nps/")):
                fail(errors, f"/archive/nps/: advertises generated fallback {alternate_route}")

    homepage = pages.get("/")
    if homepage is None:
        fail(errors, "/: homepage missing")
    elif not homepage.description or "{ loading=lazy }" in homepage.description:
        fail(errors, "/: homepage meta description is missing or malformed")

    robot_candidates = list(SITE_DIR.glob("RobotCtrl_Core-*/index.html"))
    if robot_candidates:
        robot = parse_page(robot_candidates[0])
        if not robot.description or len(robot.description) < 55:
            fail(errors, f"{robot.route}: page-specific description is missing/too short")
        elif homepage and robot.description == homepage.description:
            fail(errors, f"{robot.route}: fell back to generic homepage/site description")

    not_found_path = SITE_DIR / "404.html"
    if not_found_path.is_file():
        not_found_html = not_found_path.read_text(encoding="utf-8")
        parser = SignalParser()
        parser.feed(not_found_html)
        if (parser.html_lang or "").lower() != "zh":
            fail(errors, f"404.html language leaked from another locale: {parser.html_lang!r}")
        if "noindex" not in (parser.robots or "").lower():
            fail(errors, "404.html is missing robots noindex")
        if "hreflang=" in not_found_html.lower():
            fail(errors, "404.html contains stale language alternates")
    else:
        fail(errors, "404.html is missing")

    validate_rss(errors, "feed_rss_created.xml")
    validate_rss(errors, "feed_rss_updated.xml")

    robots_path = SITE_DIR / "robots.txt"
    if not robots_path.is_file():
        fail(errors, "robots.txt is missing")
    else:
        robots = robots_path.read_text(encoding="utf-8")
        if "Sitemap: https://wiki-power.com/sitemap.xml" not in robots:
            fail(errors, "robots.txt does not advertise the canonical sitemap")

    representative = []
    if homepage:
        representative.append(homepage)
    if robot_candidates:
        representative.append(parse_page(robot_candidates[0]))
    for page in representative:
        if "pagead2.googlesyndication.com/pagead/js/adsbygoogle.js" in page.html:
            fail(errors, f"{page.route}: AdSense library is statically injected instead of lazy-loaded")
        if "viewer.altium.com/client/static/js/embed.js" in page.html:
            fail(errors, f"{page.route}: Altium viewer is statically injected instead of conditional")

    if errors:
        print(f"Site output validation FAILED with {len(errors)} issue(s):", file=sys.stderr)
        for error in errors[:80]:
            print(f" - {error}", file=sys.stderr)
        if len(errors) > 80:
            print(f" - ... {len(errors) - 80} more", file=sys.stderr)
        return 1

    print(
        "Site output validation passed: "
        f"{len(pages)} pages, {noncanonical} noncanonical fallback pages, "
        f"{len(sitemap)} sitemap locations, {hreflang_links} hreflang links."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
