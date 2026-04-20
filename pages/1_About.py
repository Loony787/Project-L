import pandas as pd
import streamlit as st
st.set_page_config(layout="wide",initial_sidebar_state="expanded")
st.page_link("Portfolio.py", label="Home")

if st.session_state.get('role') is None:
    st.switch_page("Portfolio.py")


st.title("ABOUT",text_alignment="center")
with st.expander("What is this about?"):
    st.markdown("This Website is a small project of mine. The main motivation was to do a small programming project. Additionally its to show possible recruiters some skills.")
    st.markdown("I also didnt want to make the 500th to-do list or something i wanted to do something I would interact with if I saw it in an application.")
with st.expander("What is my goal?"):
    st.markdown("I want to fill this step for step with some analysis of data sets")
with st.expander("What am I interested in?"):
    st.markdown("I like to analyse data and try to draw possible implications from it or to see some funny correlations. Besides that im a football fan.")