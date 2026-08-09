import re

_ARTICLE_RE = re.compile(
    r'(?P<open><article\b[^>]*\bclass=(?:"[^"]*\bmd-content__inner\b[^"]*"|\'[^\']*\bmd-content__inner\b[^\']*\'|[^\s>]*md-content__inner[^\s>]*)[^>]*>)'
    r'(?P<body>.*?)'
    r'(?P<close></article>)',
    re.IGNORECASE | re.DOTALL,
)
_IMG_RE = re.compile(r'<img\b[^>]*>', re.IGNORECASE)
_LOADING_RE = re.compile(r'\sloading\s*=', re.IGNORECASE)
_DECODING_RE = re.compile(r'\sdecoding\s*=', re.IGNORECASE)


def optimize_article_images(output: str) -> str:
    """Lazy-load only article images after the first image on each page.

    The first article image is intentionally left untouched because it is the
    most likely image to contribute to LCP. Theme chrome (logo, navigation,
    social icons) lives outside the article element and is never modified.
    Explicit author-provided loading/decoding attributes are preserved.
    """

    def rewrite_article(match: re.Match[str]) -> str:
        seen_images = 0

        def rewrite_image(image_match: re.Match[str]) -> str:
            nonlocal seen_images
            seen_images += 1
            tag = image_match.group(0)
            if seen_images == 1:
                return tag

            additions = []
            if not _LOADING_RE.search(tag):
                additions.append('loading="lazy"')
            if not _DECODING_RE.search(tag):
                additions.append('decoding="async"')
            if not additions:
                return tag

            insert = " " + " ".join(additions)
            if tag.endswith("/>"):
                return tag[:-2].rstrip() + insert + " />"
            return tag[:-1].rstrip() + insert + ">"

        body = _IMG_RE.sub(rewrite_image, match.group("body"))
        return match.group("open") + body + match.group("close")

    return _ARTICLE_RE.sub(rewrite_article, output)
