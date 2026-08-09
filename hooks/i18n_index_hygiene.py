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
        config.extra["alternate"] = []
    return context


def on_page_context(context, page, config, **kwargs):
    """Unify canonical and hreflang signals for real translations and fallbacks."""
    _canonicalize_fallback(page)
    _filter_page_alternates(page, config)
    return context


def on_post_page(output, page, config, **kwargs):
    """Correct the document language for English-primary files kept on root URLs."""
    file = page.file
    if (
        getattr(file, "locale", None) == "zh"
        and _source_name(file) in ENGLISH_ORIGINALS
    ):
        output = _HTML_LANG_ZH_RE.sub(r"\1en", output, count=1)
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
    """Advertise only real source/translation URLs, never generated fallbacks."""
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

    config.extra["alternate"] = alternates


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
