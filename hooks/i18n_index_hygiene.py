import re

_ROBOTS_META = '<meta name="robots" content="noindex, follow">'
_HEAD_CLOSE_RE = re.compile(r"</head\s*>", re.IGNORECASE)
_TARGET_PREFIXES = ("archive/", "unlist/")


def on_post_page(output, page, **kwargs):
    """Noindex only non-default-language fallback copies of legacy pages."""
    file = page.file
    source_path = getattr(file, "norm_src_uri", file.src_uri)
    source_locale = getattr(file, "locale", None)
    output_locale = getattr(file, "locale_alternate_of", None)

    if not _is_fallback_legacy_page(
        source_path=source_path,
        source_locale=source_locale,
        output_locale=output_locale,
    ):
        return output

    if 'name="robots"' in output or "name='robots'" in output:
        return output

    return _HEAD_CLOSE_RE.sub(f"  {_ROBOTS_META}\n</head>", output, count=1)


def _is_fallback_legacy_page(source_path, source_locale, output_locale):
    if not source_path.startswith(_TARGET_PREFIXES):
        return False
    if not source_locale or not output_locale:
        return False
    return source_locale != output_locale
