from urllib.parse import urlsplit, urlunsplit

_TARGET_PREFIXES = ("archive/", "unlist/", "blog/")
_TARGET_EXACT = {"机器学习入门-基础流程.md"}


def on_page_context(context, page, config, **kwargs):
    """Point audited duplicate fallback pages at their default-language URL."""
    file = page.file
    source_path = getattr(file, "norm_src_uri", file.src_uri)
    source_locale = getattr(file, "locale", None)
    output_locale = getattr(file, "locale_alternate_of", None)

    if not _is_duplicate_fallback(source_path, source_locale, output_locale):
        return context

    canonical = page.canonical_url
    if not canonical:
        return context

    parts = urlsplit(canonical)
    locale_prefix = f"/{output_locale}/"
    if not parts.path.startswith(locale_prefix):
        return context

    default_path = "/" + parts.path[len(locale_prefix):]
    page.canonical_url = urlunsplit((parts.scheme, parts.netloc, default_path, "", ""))
    return context


def _is_duplicate_fallback(source_path, source_locale, output_locale):
    if not source_locale or not output_locale or source_locale == output_locale:
        return False
    return source_path.startswith(_TARGET_PREFIXES) or source_path in _TARGET_EXACT
