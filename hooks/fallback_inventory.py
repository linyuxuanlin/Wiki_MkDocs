import html
import re

_HEAD_CLOSE_RE = re.compile(r"</head\s*>", re.IGNORECASE)


def on_post_page(output, page, **kwargs):
    file = page.file
    source_locale = getattr(file, "locale", None)
    output_locale = getattr(file, "locale_alternate_of", None)

    if not source_locale or not output_locale or source_locale == output_locale:
        return output

    source_path = getattr(file, "norm_src_uri", file.src_uri)
    marker = (
        '<!-- i18n-fallback '
        f'source="{html.escape(str(source_locale), quote=True)}" '
        f'output="{html.escape(str(output_locale), quote=True)}" '
        f'path="{html.escape(str(source_path), quote=True)}" -->'
    )
    return _HEAD_CLOSE_RE.sub(f"  {marker}\n</head>", output, count=1)
