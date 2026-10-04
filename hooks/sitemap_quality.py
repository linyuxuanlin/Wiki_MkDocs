import gzip
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit

from mkdocs.plugins import event_priority

_LOCALES = ("en", "es", "ar")
_FRONTMATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.DOTALL)
_MARKDOWN_WRAPPER_RE = re.compile(r"^\s*(?:`{3,}|~{3,})\s*markdown\s*$", re.IGNORECASE)
_SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
_XHTML_NS = "http://www.w3.org/1999/xhtml"

ET.register_namespace("", _SITEMAP_NS)
ET.register_namespace("xhtml", _XHTML_NS)


def _first_nonempty_line(text):
    text = _FRONTMATTER_RE.sub("", text, count=1)
    for line in text.splitlines():
        if line.strip():
            return line
    return ""


def _starts_markdown_wrapper(path):
    try:
        text = Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return False
    return bool(_MARKDOWN_WRAPPER_RE.match(_first_nonempty_line(text)))


def _route_for(locale, relative_path):
    relative = Path(relative_path)
    if relative.name.lower() == "index.md":
        stem = relative.parent.as_posix()
    else:
        stem = relative.with_suffix("").as_posix()
    if stem in {"", "."}:
        return f"/{locale}/"
    return f"/{locale}/{stem}/"


def _quarantined_routes(config):
    docs_dir = Path(config.docs_dir)
    zh_dir = docs_dir / "zh"
    routes = set()

    for locale in _LOCALES:
        locale_dir = docs_dir / locale
        if not locale_dir.is_dir():
            continue

        for translated in locale_dir.rglob("*.md"):
            relative = translated.relative_to(locale_dir)
            source = zh_dir / relative
            if not source.is_file():
                continue
            if not _starts_markdown_wrapper(translated):
                continue
            if _starts_markdown_wrapper(source):
                continue
            routes.add(_route_for(locale, relative))

    return routes


def _normalized_path(url):
    path = unquote(urlsplit(url).path) or "/"
    if not path.startswith("/"):
        path = "/" + path
    if path != "/" and not path.endswith("/"):
        path += "/"
    return path


def _rewrite_sitemap(path, quarantined_routes):
    tree = ET.parse(path)
    root = tree.getroot()
    removed_locations = 0
    removed_alternates = 0

    for url_node in list(root.findall(f"{{{_SITEMAP_NS}}}url")):
        loc = url_node.find(f"{{{_SITEMAP_NS}}}loc")
        if loc is not None and loc.text and _normalized_path(loc.text) in quarantined_routes:
            root.remove(url_node)
            removed_locations += 1
            continue

        for link in list(url_node.findall(f"{{{_XHTML_NS}}}link")):
            href = link.attrib.get("href")
            if href and _normalized_path(href) in quarantined_routes:
                url_node.remove(link)
                removed_alternates += 1

    payload = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    path.write_bytes(payload)
    return payload, removed_locations, removed_alternates


@event_priority(-200)
def on_post_build(config, **kwargs):
    """Finalize sitemap after static-i18n has completed recursive locale builds."""
    sitemap_path = Path(config.site_dir) / "sitemap.xml"
    if not sitemap_path.is_file():
        return

    quarantined_routes = _quarantined_routes(config)
    if not quarantined_routes:
        return

    payload, _removed_locations, _removed_alternates = _rewrite_sitemap(
        sitemap_path, quarantined_routes
    )

    gzip_path = Path(config.site_dir) / "sitemap.xml.gz"
    if gzip_path.exists():
        with gzip.open(gzip_path, "wb") as handle:
            handle.write(payload)
