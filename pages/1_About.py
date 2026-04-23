import pandas as pd
import streamlit as st
import time
st.set_page_config(layout="wide",initial_sidebar_state="expanded")
def Start():
    if st.session_state.get('role') is None:
        st.switch_page("Portfolio.py")

col1, col2, col3, col4, col5 = st.columns(5)
with col3.spinner("Loading...",show_time=True):
    time.sleep(1.5)

st.page_link("Portfolio.py", label="Home")
st.title("About",text_alignment="center")
#Content------------------------------------------------------------------------------------------------

def Content():
    col1, col2, col3 = st.columns([1,3,1])
    with col2.expander("What is this about?",expanded=True):
        st.markdown("This website is a personal project. " \
                    "Its primary purpose was to build a small programming project, " \
                    "while also providing a way to showcase my skills to potential recruiters. " \
                    "I intentionally chose a project which I would actively use myself, rather than something purely technical like a to-do list.")

    with col2.expander("What does the roadmap look like?",expanded=True):
        st.markdown("Once the core functionality is stable, I plan to analyze datasets that I find interesting, relevant and / or funny. " \
                    "This could include comparing football clubs in terms of market value or transfer balance relative to performance (wins / trophies / revenue). " \
                    "From a technical perspective, I aim to integrate APIs to enable automated data updates and more dynamic analyses.")    

    with col2.expander("What am I interested in?",expanded=True):
        st.markdown("I am particularly interested in analyzing data to derive insights from it and explain underlying patterns or differences. " \
                    "There is also a particular focus on identifying inefficiencies, especially in areas such as infrastructure, traffic and administrative processes, " \
                    "where significant optimization potential often exists. " \
                    "The focus stems from everyday exposure to issues such as long delays, traffic congestion, and inefficient administrative processes.")


Start()
Content()
