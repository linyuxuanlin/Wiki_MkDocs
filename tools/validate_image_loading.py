#!/usr/bin/env python3
"""Validate conservative article image loading behavior in generated HTML."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

from hooks.image_loading import optimize_article_images

SITE_DIR = Path("site")
_IMG_TAG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
_LOADING_LAZY_RE = re.compile(r"\sloading=(?:\"lazy\"|'lazy'|lazy)(?=[\s>])", re.IGNORECASE)
_DECODING_ASYNC_RE = re.compile(r"\sdecoding=(?:\"async\"|'async'|async)(?=[\s>])", re.IGNORECASE)
_LOADING_ANY_RE = re.compile(r"\sloading\s*=", re.IGNORECASE)
_DECODING_ANY_RE = re.compile(r"\sdecoding\s*=", re.IGNORECASE)


class ArticleImageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.article_depth = 0
        self.images: list[dict[str, str | None]] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        values = {key.lower(): value for key, value in attrs if key}
        if tag.lower() == "article":
            classes = (values.get("class") or "").split()
            if "md-content__inner" in classes:
                self.article_depth += 1
        elif tag.lower() == "img" and self.article_depth:
            self.images.append(values)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "article" and self.article_depth:
            self.article_depth -= 1


def synthetic_test() -> list[str]:
    errors: list[str] = []
    source = (
        '<header><img src="logo.png"></header>'
        '<article class="md-content__inner md-typeset">'
        '<img src="hero.png">'
        '<p><img src="later.png"></p>'
        '<img src="explicit.png" loading="eager">'
        '</article>'
    )
    result = optimize_article_images(source)
    tags = _IMG_TAG_RE.findall(result)

    if tags[0] != '<img src="logo.png">':
        errors.append("theme image was modified")
    if tags[1] != '<img src="hero.png">':
        errors.append("first article image was modified")
    if not _LOADING_LAZY_RE.search(tags[2]) or not _DECODING_ASYNC_RE.search(tags[2]):
        errors.append("later article image did not receive lazy/async attributes")
    if 'loading="eager"' not in tags[3]:
        errors.append("explicit author loading attribute was overwritten")
    if not _DECODING_ASYNC_RE.search(tags[3]):
        errors.append("missing decoding attribute was not added to explicit-loading image")

    return errors


def main() -> int:
    errors = synthetic_test()
    if not SITE_DIR.is_dir():
        print("site/ is missing; run `mkdocs build --clean` first.", file=sys.stderr)
        return 2

    html_files = sorted(SITE_DIR.rglob("*.html"))
    article_images = 0
    pages_with_images = 0
    pages_with_multiple_images = 0
    later_images = 0
    lazy_later_images = 0
    explicit_nonlazy_later_images = 0

    for path in html_files:
        html = path.read_text(encoding="utf-8", errors="replace")
        parser = ArticleImageParser()
        parser.feed(html)
        images = parser.images
        if not images:
            continue

        pages_with_images += 1
        article_images += len(images)
        if len(images) < 2:
            continue

        pages_with_multiple_images += 1
        for attrs in images[1:]:
            later_images += 1
            loading = (attrs.get("loading") or "").lower()
            decoding = (attrs.get("decoding") or "").lower()

            if loading == "lazy":
                lazy_later_images += 1
            elif loading:
                explicit_nonlazy_later_images += 1
            else:
                errors.append(
                    f"{path.relative_to(SITE_DIR)}: later article image missing loading attribute"
                )

            if not decoding:
                errors.append(
                    f"{path.relative_to(SITE_DIR)}: later article image missing decoding attribute"
                )

    if errors:
        print(f"Image loading validation FAILED with {len(errors)} issue(s):", file=sys.stderr)
        for error in errors[:80]:
            print(f" - {error}", file=sys.stderr)
        if len(errors) > 80:
            print(f" - ... {len(errors) - 80} more", file=sys.stderr)
        return 1

    print(
        "Image loading validation passed: "
        f"{article_images} article images across {pages_with_images} pages; "
        f"{later_images} non-leading images across {pages_with_multiple_images} multi-image pages; "
        f"{lazy_later_images} lazy-loaded, "
        f"{explicit_nonlazy_later_images} retained explicit non-lazy loading."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
