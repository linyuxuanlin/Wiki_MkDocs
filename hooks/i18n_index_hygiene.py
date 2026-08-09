import re
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit, urlunsplit

from mkdocs.plugins import event_priority

# Files stored in the default zh source tree whose primary visible content is English.
# They stay on their established root URLs, but are advertised semantically as English.
ENGLISH_ORIGINALS = frozenset(
    {
        "ADC-Dynamic_Parameters.md",
        "ADC-Static_Parameters.md",
        "Basics_of_Fourier_Transform.md",
        "Basics_of_Mixed_Signal_Test.md",
        "Basics_of_Signal_and_Power_Integrity.md",
        "Basics_of_VBT_Syntax.md",
        "CPR-Fundamental.md",
        "Continuity_Test.md",
        "DAC-Dynamic_Parameters.md",
        "DAC-Static_Parameters.md",
        "DC_Parameters.md",
        "Digital_Functional_Test.md",
        "IDD_Test.md",
        "Leakage_Test.md",
        "Level_Threshold_Test.md",
        "Pattern_Syntax_Notes.md",
        "Personal_Onboarding_Workflow_(Windows).md",
        "Tester_Alarms.md",
        "TheExec(The_Executive).md",
        "TheHdw(The_Hardware).md",
        "Troubleshooting_of_ADC_and_DAC.md",
        "WeChat.md",
    }
)

_TRANSLATION_LOCALES = frozenset({"en", "es", "ar"})
_TRANSLATION_QUALITY_CACHE = {}
_MARKDOWN_WRAPPER_RE = re.compile(r"^\s*(?:`{3,}|~{3,})\s*markdown\s*$", re.IGNORECASE)
_NO_INDEX_RE = re.compile(
    r'<meta\b[^>]*\bname=(?:"robots"|\'robots\'|robots)[^>]*\bcontent=(?:"[^"]*noindex[^"]*"|\'[^\']*noindex[^\']*\'|[^\s>]*noindex[^\s>]*)[^>]*>',
    re.IGNORECASE,
)
_QUARANTINE_META = '<meta name="robots" content="noindex, follow">'

_DEFAULT_SHARED_OUTPUTS = {}
_SHARED_OUTPUT_NAMES = (
    "404.html",
    "feed_rss_created.xml",
    "feed_rss_updated.xml",
)
_HTML_LANG_ZH_RE = re.compile(
    r'(<html\b[^>]*\blang=)(?:"zh"|\'zh\'|zh)(?=[\s>])',
    re.IGNORECASE,
)


def on_config(config, **kwargs):
    """Expose the audited English-original list to the sitemap template."""
    config.extra["english_originals"] = sorted(ENGLISH_ORIGINALS)
    return config


def on_template_context(context, template_name, config, **kwargs):
    """Keep the shared 404 template free of stale page-level language alternates."""
    if template_name == "404.html":
        config.extra.alternate = []
    return context


def on_page_context(context, page, config, **kwargs):
    """Unify canonical/hreflang signals and mark deterministically bad translations."""
    if _is_malformed_translation(page.file, config):
        page.meta["_translation_quality_quarantine"] = True

    _canonicalize_fallback(page)
    _filter_page_alternates(page, config)
    return context


def on_post_page(output, page, config, **kwargs):
    """Apply final document-language and translation-quality output hygiene."""
    file = page.file
    if (
        getattr(file, "locale", None) == "zh"
        and _source_name(file) in ENGLISH_ORIGINALS
    ):
        output = _HTML_LANG_ZH_RE.sub(r"\1en", output, count=1)

    if _is_malformed_translation(file, config):
        output = _ensure_noindex(output)

    return output


@event_priority(-50)
def on_post_build(config, **kwargs):
    """Preserve default-locale shared root outputs across recursive i18n builds.

    mkdocs-static-i18n performs additional locale builds into the same site_dir.
    Files such as 404.html and RSS feeds are shared root outputs, so later locale
    builds otherwise overwrite the default-locale versions.
    """
    i18n = config.plugins.get("i18n")
    if i18n is None:
        return

    site_dir = Path(config.site_dir)
    if not getattr(i18n, "building", False):
        _DEFAULT_SHARED_OUTPUTS.clear()
        for name in _SHARED_OUTPUT_NAMES:
            path = site_dir / name
            if path.is_file():
                _DEFAULT_SHARED_OUTPUTS[name] = path.read_bytes()
        return

    for name, content in _DEFAULT_SHARED_OUTPUTS.items():
        path = site_dir / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)


def _ensure_noindex(output):
    if _NO_INDEX_RE.search(output):
        return output

    closing_head = output.lower().find("</head>")
    if closing_head < 0:
        return output

    return output[:closing_head] + _QUARANTINE_META + output[closing_head:]


def _first_nonempty_line(text):
    for line in text.splitlines():
        if line.strip():
            return line
    return ""


def _starts_markdown_wrapper(path):
    try:
        text = Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeError, TypeError):
        return False
    return bool(_MARKDOWN_WRAPPER_RE.match(_first_nonempty_line(text)))


def _is_malformed_translation(file, config):
    """Detect a zero-ambiguity legacy translation corruption pattern.

    Some historical machine translations begin with a ` ```markdown ` or
    ` ````markdown ` fence even though the corresponding zh source does not.
    Material then renders a large part of the article as code. Only that exact,
    deterministic pattern is quarantined here; heuristic quality signals are not.
    """
    locale = getattr(file, "locale", None)
    if locale not in _TRANSLATION_LOCALES:
        return False

    translated_path = getattr(file, "abs_src_path", None)
    normalized_source = getattr(file, "norm_src_uri", None)
    if not translated_path or not normalized_source:
        return False

    cache_key = (str(translated_path), str(normalized_source), str(config.docs_dir))
    cached = _TRANSLATION_QUALITY_CACHE.get(cache_key)
    if cached is not None:
        return cached

    translated_has_wrapper = _starts_markdown_wrapper(translated_path)
    if not translated_has_wrapper:
        _TRANSLATION_QUALITY_CACHE[cache_key] = False
        return False

    zh_path = Path(config.docs_dir) / "zh" / PurePosixPath(normalized_source)
    if not zh_path.is_file():
        _TRANSLATION_QUALITY_CACHE[cache_key] = False
        return False

    malformed = not _starts_markdown_wrapper(zh_path)
    _TRANSLATION_QUALITY_CACHE[cache_key] = malformed
    return malformed


def _canonicalize_fallback(page):
    file = page.file
    source_locale = getattr(file, "locale", None)
    output_locale = getattr(file, "locale_alternate_of", None)

    if not source_locale or not output_locale or source_locale == output_locale:
        return

    canonical = page.canonical_url
    if not canonical:
        return

    parts = urlsplit(canonical)
    locale_prefix = f"/{output_locale}/"
    if not parts.path.startswith(locale_prefix):
        return

    source_path = "/" + parts.path[len(locale_prefix):]
    page.canonical_url = urlunsplit((parts.scheme, parts.netloc, source_path, "", ""))


def _filter_page_alternates(page, config):
    """Advertise only real, structurally valid translations; never fallbacks."""
    file = page.file
    file_alternates = getattr(file, "alternates", None)
    i18n = config.plugins.get("i18n")
    if not file_alternates or i18n is None:
        return

    alternates = []
    seen_languages = set()

    for locale in i18n.all_languages:
        alternate_file = file_alternates.get(locale)
        if alternate_file is None:
            continue

        # If the alternate's source locale differs from the emitted locale,
        # static-i18n generated a fallback copy rather than a real translation.
        if getattr(alternate_file, "locale", None) != locale:
            continue

        # Deterministically malformed legacy translations remain reachable but
        # are not advertised as valid localized alternatives.
        if _is_malformed_translation(alternate_file, config):
            continue

        semantic_language = _semantic_language(locale, alternate_file)
        if semantic_language in seen_languages:
            continue

        language_config = i18n.get_language_config(semantic_language)
        alternates.append(
            {
                "name": language_config.name,
                "link": alternate_file.url,
                "lang": semantic_language,
            }
        )
        seen_languages.add(semantic_language)

    # static-i18n itself updates this LegacyConfig using attribute assignment.
    # Use the same write path so Material's template sees the replacement in
    # the current page context rather than the plugin's precomputed fallback list.
    config.extra.alternate = alternates


def _semantic_language(locale, file):
    if locale == "zh" and _source_name(file) in ENGLISH_ORIGINALS:
        return "en"
    return locale


def _source_name(file):
    source_uri = (
        getattr(file, "norm_src_uri", None)
        or getattr(file, "src_uri", None)
        or ""
    )
    return PurePosixPath(source_uri).name
