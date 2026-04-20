import pandas as pd
import streamlit as st
st.set_page_config(layout="wide",initial_sidebar_state="expanded")
st.page_link("Portfolio.py", label="Home")

if st.session_state.get('role') is None:
    st.switch_page("Portfolio.py")

st.title("Applications")
st.header("X")
