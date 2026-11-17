"""Demo app: streamlit run example.py"""

import streamlit as st

from st_show_more import st_show_more

LOREM = (
    "**Lorem ipsum** dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor "
    "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud "
    "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n\n"
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat "
    "nulla pariatur. [Excepteur sint](https://streamlit.io) occaecat cupidatat non proident.\n\n"
    "- sunt in culpa\n- qui officia\n- deserunt mollit"
)

st.title("st_show_more")

with st.container(border=True):
    st.subheader("Preview as a number of characters")
    st_show_more(LOREM, preview=120)

    with st.expander(":material/code: view code"):
        st.code(
            """
st.subheader("Preview as a number of characters")
st_show_more(LOREM, preview=120)""",
            language="python",
        )

with st.container(border=True):
    st.subheader("Preview as a custom string, custom labels")
    st_show_more(LOREM, preview="A *hand-written* summary of the text.", more_label="Leggi tutto", less_label="Chiudi")

    with st.expander(":material/code: view code"):
        st.code(
            """
st.subheader("Preview as a custom string, custom labels")
st_show_more(LOREM, preview="A *hand-written* summary of the text.", more_label="Leggi tutto", less_label="Chiudi")""",
            language="python",
        )

with st.container(border=True):
    st.subheader("One-way expansion (no \"Show less\")")
    st_show_more(LOREM, preview=60, less_label=None)

    with st.expander(":material/code: view code"):
        st.code(
            """
st.subheader("One-way expansion (no "Show less")")
st_show_more(LOREM, preview=60, less_label=None)"""
        )

with st.container(border=True):
    st.subheader("Color and size")
    st_show_more(LOREM, preview=120, color="gray", size=12)
    st_show_more(LOREM, preview=120, color="blue", size=20)

    with st.expander(":material/code: view code"):
        st.code(
            """
st.subheader("Color and size")
st_show_more(LOREM, preview=120, color="gray", size=12)
st_show_more(LOREM, preview=120, color="blue", size=20)""",
            language="python",
        )

with st.container(border=True):
    st.subheader("Short text: nothing to hide => no button")
    st_show_more("Just a short sentence.", preview=120)

    with st.expander(":material/code: view code"):
        st.code(
            """
st.subheader("Short text: nothing to hide => no button")
st_show_more("Just a short sentence.", preview=120)""",
            language="python",
        )

st.info("State survives reruns, try clicking the button below to rerun the app and see that the state is preserved.")
if st.button("Rerun the app"):
    st.rerun()
