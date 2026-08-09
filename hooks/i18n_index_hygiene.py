from urllib.parse import urlsplit, urlunsplit


def on_page_context(context, page, config, **kwargs):
    """Canonicalize any generated i18n fallback copy to its source/default URL."""
    file = page.file
    source_locale = getattr(file, "locale", None)
    output_locale = getattr(file, "locale_alternate_of", None)

    if not source_locale or not output_locale or source_locale == output_locale:
        return context

    canonical = page.canonical_url
    if not canonical:
        return context

    parts = urlsplit(canonical)
    locale_prefix = f"/{output_locale}/"
    if not parts.path.startswith(locale_prefix):
        return context

    source_path = "/" + parts.path[len(locale_prefix):]
    page.canonical_url = urlunsplit((parts.scheme, parts.netloc, source_path, "", ""))
    return context
