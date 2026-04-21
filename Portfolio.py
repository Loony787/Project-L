import streamlit as st
import pandas as pd
import gspread
from datetime import datetime

st.set_page_config(layout="wide",initial_sidebar_state="expanded")
st.title("Project: L",text_alignment="center")
st.divider()

credentials = st.secrets["gcp_service_account"]
gc = gspread.service_account_from_dict(credentials)
sheet = gc.open("Project-L").sheet1

def Pop_Up():
    st.session_state.role = None
    col1, col2, col3 = st.columns(3)
    role = col1.button("RECRUITER",width="stretch")
    role = col2.button("GUEST", width="stretch")
    role = col3.button("FRIEND", width="stretch")
    st.warning("CHOOSE AN OPTION TO ENTER!:D")
    if role == "RECRUITER" or role == "GUEST" or role == "FRIEND":
        st.session_state.role = role 
        sheet.append_row([datetime.now().strftime("%Y-%m-%d %H:%M:%S"),st.session_state.role])

def Main_Menu():
    st.header("Menu",text_alignment="center")
    st.markdown("Welcome to my page! Here you have a little overview on which pages are available.\nFeel free to discover all of them!")
    st.warning("Work is currently in progress. Most of the pages have not been filled yet.")
    #Menu
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
            st.switch_page("pages/3_Application Statistics.py")
        if st.button("CV",width="stretch"):
            st.switch_page("pages/4_CV.py")


if 'role' not in st.session_state or st.session_state.role is None:
    Pop_Up()
else:
    Main_Menu()