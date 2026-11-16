"""Demo app: streamlit run example.py"""

import streamlit as st

from streamlit_show_more import show_more

LOREM = (
    "**Lorem ipsum** dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor "
    "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud "
    "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n\n"
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat "
    "nulla pariatur. [Excepteur sint](https://streamlit.io) occaecat cupidatat non proident.\n\n"
    "- sunt in culpa\n- qui officia\n- deserunt mollit"
)

st.title("streamlit-show-more")

st.subheader("Preview as a number of characters")
show_more(LOREM, preview=120)

st.subheader("Preview as a custom string, custom labels")
show_more(LOREM, preview="A *hand-written* summary of the text.", more_label="Leggi tutto", less_label="Chiudi")

st.subheader("One-way expansion (no \"Show less\")")
show_more(LOREM, preview=60, less_label=None)

st.subheader("Color and size")
show_more(LOREM, preview=120, color="gray", size=12)
show_more(LOREM, preview=120, color="blue", size=20)

st.subheader("Short text: nothing to hide, no button")
show_more("Just a short sentence.", preview=120)

st.subheader("State survives reruns")
st.button("Rerun the app")
