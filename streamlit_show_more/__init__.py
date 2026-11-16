"""streamlit-show-more: st.write-like text with an inline "Show more" button."""

from __future__ import annotations

from pathlib import Path

import streamlit as st
from markdown_it import MarkdownIt

__all__ = ["show_more", "make_preview"]
__version__ = "0.1.0"

_FRONTEND = Path(__file__).parent / "frontend"

# Registered once at import time; every show_more() call mounts a new instance.
_component = st.components.v2.component(
    "streamlit_show_more.show_more",
    html='<div class="ssm-root"></div>',
    css=(_FRONTEND / "show_more.css").read_text(encoding="utf-8"),
    js=(_FRONTEND / "show_more.js").read_text(encoding="utf-8"),
)

# Raw HTML in the text is escaped unless the caller opts in (same default as st.write).
_MD_SAFE = MarkdownIt("commonmark", {"html": False, "linkify": False}).enable(["table", "strikethrough"])
_MD_HTML = MarkdownIt("commonmark", {"html": True, "linkify": False}).enable(["table", "strikethrough"])


def make_preview(text: str, n_chars: int, ellipsis: str = "…") -> tuple[str, bool]:
    """Cut ``text`` to at most ``n_chars`` characters, preferring a word boundary.

    Returns ``(preview, truncated)``. When the text already fits, it is returned
    unchanged with ``truncated=False``.
    """
    if n_chars < 0:
        raise ValueError("preview length must be >= 0")
    if len(text) <= n_chars:
        return text, False
    cut = text[:n_chars]
    # Don't break a word in half, unless that would throw away most of the preview.
    if not text[n_chars].isspace():
        boundary = max(cut.rfind(" "), cut.rfind("\n"))
        if boundary >= n_chars * 0.6:
            cut = cut[:boundary]
    # "elit,…" reads badly: drop dangling punctuation before the ellipsis.
    return cut.rstrip().rstrip(",;:.-–—") + ellipsis, True


def show_more(
    text: str,
    preview: str | int = 200,
    more_label: str = "Show more",
    less_label: str | None = "Show less",
    *,
    color: str | None = None,
    size: int | float | str | None = None,
    expanded: bool = False,
    unsafe_allow_html: bool = False,
    key: str | None = None,
) -> None:
    """Write ``text`` as Markdown, collapsed to a preview with a "Show more" button.

    Parameters
    ----------
    text : str
        The full text (Markdown), shown once the user clicks the button.
    preview : str or int
        What to show while collapsed. An ``int`` takes the first N characters of
        ``text`` (cut at a word boundary, with a trailing ellipsis); if ``text``
        is not longer than N it is shown in full, without a button. A ``str`` is
        used as the preview as-is (Markdown).
    more_label : str
        Label of the button that expands the text.
    less_label : str or None
        Label of the button that collapses the text again. ``None`` makes the
        expansion one-way (no button once expanded).
    color : str or None
        Text color, as any CSS color: a name (``"gray"``, ``"blue"``), a hex
        code (``"#ff4b4b"``) or a function (``"rgb(...)"``). ``None`` uses the
        theme's text color. Links and the button keep the theme's link color.
    size : int, float, str or None
        Font size. A number is taken as pixels (``12`` -> ``12px``); a string is
        used as a CSS length (``"0.875rem"``). ``None`` uses the app's size.
    expanded : bool
        Initial state.
    unsafe_allow_html : bool
        Render raw HTML contained in the text instead of escaping it. Only
        enable this for content you trust.
    key : str or None
        Optional unique key for the component instance.
    """
    text = "" if text is None else str(text)

    # bool is an int subclass: reject it rather than treating True as "1 char".
    if isinstance(preview, bool) or not isinstance(preview, (int, str)):
        raise TypeError("preview must be a str or an int (number of characters)")
    if isinstance(preview, int):
        preview_text, truncated = make_preview(text, preview)
    else:
        preview_text, truncated = preview, preview != text

    if color is not None and not isinstance(color, str):
        raise TypeError("color must be a CSS color string")
    if isinstance(size, bool) or not isinstance(size, (int, float, str, type(None))):
        raise TypeError("size must be a number of pixels or a CSS length string")
    if isinstance(size, (int, float)):
        if size <= 0:
            raise ValueError("size must be > 0")
        size = f"{size:g}px"

    md = _MD_HTML if unsafe_allow_html else _MD_SAFE
    _component(
        key=key,
        data={
            "full_html": md.render(text),
            "preview_html": md.render(preview_text) if truncated else "",
            "truncated": truncated,
            "more_label": more_label,
            "less_label": less_label,
            "color": color,
            "size": size,
            "expanded": bool(expanded),
        },
    )
