# streamlit-show-more

A Streamlit component that writes Markdown text like `st.write`, collapsed to a
preview that ends with an inline **Show more** button. Clicking it reveals the
full text.

Expanding and collapsing happens in the browser: no rerun of your app, and the
state survives reruns triggered by other widgets.

## Install

```bash
pip install git+https://github.com/<your-user>/streamlit-show-more.git
```

Requires Streamlit >= 1.51 (it is built on `st.components.v2`, so it renders
inline in the page, not in an iframe, and follows the app theme).

## Usage

```python
from streamlit_show_more import show_more

# Preview = first 120 characters of the text
show_more(long_text, preview=120)

# Preview = your own text, custom button labels
show_more(long_text, preview="A short summary.", more_label="Read all", less_label="Close")
```

| Parameter           | Type            | Default       | Description |
|---------------------|-----------------|---------------|-------------|
| `text`              | `str`           | required      | Full text (Markdown). |
| `preview`           | `str` or `int`  | `200`         | `int`: first N characters of `text`, cut at a word boundary and followed by `…`. If `text` fits in N characters it is shown in full with no button. `str`: used as the preview as-is (Markdown). |
| `more_label`        | `str`           | `"Show more"` | Label of the expand button. |
| `less_label`        | `str` or `None` | `"Show less"` | Label of the collapse button. `None` = no way back once expanded. |
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
