import pandas as pd
import streamlit as st
st.set_page_config(layout="wide",initial_sidebar_state="expanded")

#Functions
st.title("Project: L", text_alignment= "center", anchor=False)
st.header("Welcome to my personal page.", anchor=False, text_alignment="center")
st.divider()

#Button size
st.markdown("""
    <style>
    .stButton button {
        font-size: 50px;
        height: 150px;
        color: white;
        background-color: grey;
    }
    </style>
""", unsafe_allow_html=True)

col1, col2= st.columns(2)
with col1:
    if st.button("About",width="stretch"):
        st.switch_page("pages/1_About.py")

    if st.button("Data Analytics",width="stretch"):
        st.switch_page("pages/2_Data Analytics.py")
with col2:
    if st.button("Application Statistics",width="stretch"):
        st.switch_page("pages/3_ApplicationStats.py")
    if st.button("CV",width="stretch"):
        st.switch_page("pages/4_CV.py")
