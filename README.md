# st_show_more
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://st-show-more.streamlit.app/)

A Streamlit component that writes Markdown text like `st.write`, collapsed to a
preview that ends with an inline **Show more** button. Clicking it reveals the
full text.

Expanding and collapsing happens in the browser: no rerun of your app, and the
state survives reruns triggered by other widgets.

https://github.com/user-attachments/assets/1feba93c-2dc0-42ce-8d9e-fd9fa72851ae

## Install

```bash
pip install st_show_more
```

Requires Streamlit >= 1.51 (it is built on `st.components.v2`, so it renders
inline in the page, not in an iframe, and follows the app theme).

## Usage

```python
from st_show_more import st_show_more

# Preview = first 120 characters of the text
st_show_more(long_text, preview=120)

# Preview = your own text, custom button labels
st_show_more(long_text, preview="A short summary.", more_label="Read all", less_label="Close")
```

| Parameter           | Type            | Default       | Description |
|---------------------|-----------------|---------------|-------------|
| `text`              | `str` or `list` or `tuple` or None | required      | Full text (Markdown). If list or tuple, the elements are joined with `joiner` to form the full text. `None` is treated as an empty string. |
| `preview`           | `str` or `int`  | `200`         | `int`: first N characters of `text`, cut at a word boundary and followed by `…`. If `text` fits in N characters it is shown in full with no button. `str`: used as the preview as-is (Markdown). If `text` is a list/tuple, the preview is applied to the number of elements in the list/tuple, not the total number of characters. |
| `more_label`        | `str`           | `"Show more"` | Label of the expand button. |
| `less_label`        | `str` or `None` | `"Show less"` | Label of the collapse button. `None` = no way back once expanded. |
| `joiner`            | `str`           | `", "`        | String used to join list/tuple elements if `text` is a list/tuple, ignored otherwise. |
| `color`             | `str` or `None` | `None`        | Text color, any CSS color: `"gray"`, `"blue"`, `"#ff4b4b"`... `None` = theme text color. Links and the button keep the theme's link color. |
| `size`              | number, `str` or `None` | `None` | Font size. A number is pixels (`12`), a string is a CSS length (`"0.875rem"`). `None` = app default. |
| `expanded`          | `bool`          | `False`       | Initial state. |
| `unsafe_allow_html` | `bool`          | `False`       | Render raw HTML found in the text instead of escaping it. Only for trusted content. |
| `key`               | `str` or `None` | `None`        | Unique key of the instance. |

## Notes

- Markdown is rendered with [markdown-it-py](https://github.com/executablebooks/markdown-it-py)
  (CommonMark + tables + strikethrough). Streamlit-only syntax such as
  `:red[text]`, `:material/icon:` and emoji shortcodes is not supported.
- An `int` preview cuts the raw Markdown source, so a cut in the middle of
  `**bold**` or a link shows the unfinished markup literally. Pass a `str`
  preview when the beginning of your text is heavily formatted.
- Links open in a new tab.

## Expanded/collapsed state

The state lives only in the browser: clicking the button never reruns your script, and the state is not sent back to Python.

| Event                                                                 | State      |
|---------------------------------------------------------------------------------------------|------------|
| Rerun of the app (any widget interaction, `st.rerun()`)               | kept       |
| `text` or `preview` changes                                           | reset      |
| `expanded` changes                                                    | reset      |
| Component removed from the page and shown again (e.g. inside an `if`, a tab or page switch) | reset |
| Full page reload (F5) or a new browser session                       | reset      |

"Reset" means back to the initial state given by `expanded` (collapsed by default). 
This also applies when a `key` is set: `key` only identifies the instance, it does not persist the state.

## Development

```bash
pip install -e .[dev]
```

```bash
pytest
```

```bash
streamlit run example.py
```

## TODO

- [ ] Protect the `main` branch.
- [ ] Refine this README.

