// Expanded/collapsed state per instance. Kept on the client so toggling never
// triggers a Streamlit rerun; it survives reruns but not remounts (even with a
// `key`, the state is reset when the component leaves the page and comes
// back) nor page reloads. See "Expanded/collapsed state" in the README.
const states = new Map();

export default function (component) {
  const { data, parentElement, key } = component;
  const root = parentElement.querySelector(".ssm-root");
  if (!root || !data) return;

  const { full_html, preview_html, truncated, more_label, less_label } = data;

  // Assigned through the style API: an invalid value is simply ignored and
  // the stylesheet default applies.
  root.style.color = "";
  root.style.fontSize = "";
  if (data.color) root.style.color = data.color;
  if (data.size) root.style.fontSize = data.size;

  // A different text is a different thing to read: start from the default again.
  const signature = `${preview_html}\u0000${full_html}`;
  const id = key ?? root;
  let state = states.get(id);
  if (!state || state.signature !== signature || state.initial !== data.expanded) {
    state = { signature, initial: data.expanded, expanded: Boolean(data.expanded) };
    states.set(id, state);
  }

  const render = () => {
    const expanded = state.expanded || !truncated;
    root.innerHTML = expanded ? full_html : preview_html;
    root.querySelectorAll("a").forEach((a) => {
      a.target = "_blank";
      a.rel = "noopener noreferrer";
    });

    const label = expanded ? less_label : more_label;
    if (!truncated || !label) return;

    const button = document.createElement("button");
    button.type = "button";
    button.className = "ssm-toggle";
    button.textContent = label;
    button.setAttribute("aria-expanded", String(expanded));
    button.addEventListener("click", () => {
      state.expanded = !expanded;
      render();
    });

    // Keep the button on the same line as the end of the text when possible.
    const last = root.lastElementChild;
    if (last && last.tagName === "P") {
      last.append(" ", button);
    } else {
      root.append(button);
    }
  };

  render();
}
