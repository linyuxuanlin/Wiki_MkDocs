import re
from html import unescape

MAX_DESCRIPTION_LENGTH = 155
MIN_DESCRIPTION_LENGTH = 55

_FENCE_RE = re.compile(r"```.*?```|~~~.*?~~~", re.DOTALL)
_HTML_RE = re.compile(r"<[^>]+>")
_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")
_INLINE_CODE_RE = re.compile(r"`([^`]+)`")
_MARKDOWN_MARKER_RE = re.compile(r"[*_~]+")
_WHITESPACE_RE = re.compile(r"\s+")


def on_page_markdown(markdown, page, **kwargs):
    """Fill page descriptions conservatively without overriding author metadata."""
    if page.meta.get("description"):
        return markdown

    description = _extract_description(markdown)
    if description:
        page.meta["description"] = description

    return markdown


def _extract_description(markdown):
    text = _FENCE_RE.sub("\n", markdown)

    for paragraph in re.split(r"\n\s*\n", text):
        cleaned = _clean_paragraph(paragraph)
        if len(cleaned) < MIN_DESCRIPTION_LENGTH:
            continue
        return _truncate(cleaned, MAX_DESCRIPTION_LENGTH)

    return None


def _clean_paragraph(paragraph):
    lines = []
    for raw_line in paragraph.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith(("#", ">", "|", "---", "+++", ":::")):
            continue
        if re.match(r"^(?:[-*+] |\d+[.)] )", line):
            continue
        if line.startswith("<") and line.endswith(">"):
            continue
        lines.append(line)

    if not lines:
        return ""

    text = " ".join(lines)
    text = _IMAGE_RE.sub("", text)
    text = _LINK_RE.sub(r"\1", text)
    text = _INLINE_CODE_RE.sub(r"\1", text)
    text = _HTML_RE.sub("", text)
    text = _MARKDOWN_MARKER_RE.sub("", text)
    text = unescape(text)
    return _WHITESPACE_RE.sub(" ", text).strip()


def _truncate(text, limit):
    if len(text) <= limit:
        return text

    shortened = text[: limit + 1]
    cut_positions = [
        shortened.rfind("。"), shortened.rfind("！"), shortened.rfind("？"),
        shortened.rfind("."), shortened.rfind("!"), shortened.rfind("?"),
        shortened.rfind(" "),
    ]
    cut = max(cut_positions)
    if cut >= int(limit * 0.65):
        return shortened[: cut + 1].strip()

    return text[: limit - 1].rstrip(" ,，;；:：") + "…"
