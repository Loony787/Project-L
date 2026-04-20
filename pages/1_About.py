import pandas as pd
import streamlit as st
st.set_page_config(layout="wide",initial_sidebar_state="expanded")
st.page_link("Portfolio.py", label="Home")

st.title("ABOUT",text_alignment="center")


def Start():
    if st.session_state.get('role') is None:
        st.switch_page("Portfolio.py")



def Content():
    with st.expander("What is this about?"):
        st.markdown("This Website is a personal project. " \
                    "Its primary purpose was to build a small programming project, " \
                    "while also providing a way to showcase my skills to potential recruiters. " \
                    "I intentionally chose a project which I actively interact with myself, rather than something purely technical like a to-do list.")

    with st.expander("What am I interested in?"):
        st.markdown("I am particularly interested in analyzing data to derive possible implications or insights from it and explain underlying patterns or differences. " \
                    "There is also a particular focus on identifying inefficiencies, especially in areas such as infrastructure, traffic and administrative processes, " \
                    "where significant optimization potential often exists." \
                    "The focus stems from everyday exposure to issues such as long delays, traffic congestion, and inefficient administrative processes.")

    with st.expander("What does the roadmap look like?"):
        st.markdown("Once the core functionality is stable, I plan to focus on analyzing datasets that I find interesting, relevant and / or funny. " \
                    "That could be something like comparing football clubs in terms of market value or transfer balance relative to performance (Wins / Trophies / Revenue). " \
                    "From a technical perspective, I aim to integrate APIs to enable automated data updates and more dynamic analyses.")

Start()
Content()
