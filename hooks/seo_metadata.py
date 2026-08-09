import re
from html import unescape

MAX_DESCRIPTION_LENGTH = 155
MIN_DESCRIPTION_LENGTH = 55

_FRONT_MATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*(?:\n|\Z)", re.DOTALL)
_FENCE_RE = re.compile(r"```.*?```|~~~.*?~~~", re.DOTALL)
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
_HTML_BLOCK_RE = re.compile(
    r"<(?:div|script|style|iframe|figure|table)\b.*?</(?:div|script|style|iframe|figure|table)>",
    re.DOTALL | re.IGNORECASE,
)
_HTML_RE = re.compile(r"<[^>]+>")
_LINKED_IMAGE_RE = re.compile(
    r"\[!\[[^\]]*\]\([^)]*\)(?:\s*\{[^{}]*\})?\]\([^)]*\)"
)
_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)(?:\s*\{[^{}]*\})?")
_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")
_ATTRIBUTE_LIST_RE = re.compile(
    r"\{\s*(?:(?:[.#][\w-]+)|(?:[\w-]+\s*=\s*(?:\"[^\"]*\"|'[^']*'|[^\s}]+)))"
    r"(?:\s+(?:(?:[.#][\w-]+)|(?:[\w-]+\s*=\s*(?:\"[^\"]*\"|'[^']*'|[^\s}]+))))*\s*\}"
)
_INLINE_CODE_RE = re.compile(r"`([^`]+)`")
_MARKDOWN_MARKER_RE = re.compile(r"[*_~]+")
_WHITESPACE_RE = re.compile(r"\s+")
_BOILERPLATE_RE = re.compile(
    r"^(?:"
    r"project\s+(?:repository|repo|online\s+preview)|"
    r"source|original(?:\s+(?:article|url|link))?|reference|references|"
    r"note:\s*this\s+project\s+is\s+included\s+in\b|"
    r"项目(?:仓库|地址|链接|预览)|在线预览|原文(?:地址|链接)?|参考(?:链接|地址)?|"
    r"注[：:]\s*本项目(?:包含|隶属|属于)"
    r")\s*[:：]?",
    re.IGNORECASE,
)


def on_page_markdown(markdown, page, **kwargs):
    """Fill page descriptions conservatively without overriding author metadata."""
    if page.meta.get("description"):
        return markdown

    description = _extract_description(markdown)
    if description:
        page.meta["description"] = description

    return markdown


def _extract_description(markdown):
    text = _FRONT_MATTER_RE.sub("", markdown)
    text = _FENCE_RE.sub("\n", text)
    text = _HTML_COMMENT_RE.sub("\n", text)
    text = _HTML_BLOCK_RE.sub("\n", text)

    for paragraph in re.split(r"\n\s*\n", text):
        cleaned = _clean_paragraph(paragraph)
        if not cleaned or _BOILERPLATE_RE.match(cleaned):
            continue
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
        if line.startswith("<"):
            continue
        lines.append(line)

    if not lines:
        return ""

    text = " ".join(lines)
    text = _LINKED_IMAGE_RE.sub("", text)
    text = _IMAGE_RE.sub("", text)
    text = _LINK_RE.sub(r"\1", text)
    text = _ATTRIBUTE_LIST_RE.sub("", text)
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
