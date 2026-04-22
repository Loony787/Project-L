import streamlit as st
import pandas as pd
import gspread
from datetime import datetime
import time

st.set_page_config(layout="wide",initial_sidebar_state="expanded")
st.title("Project: L",text_alignment="center")
st.divider()

col1, col2, col3, col4, col5 = st.columns(5)
with col3: 
    loading_placeholder = st.empty()

credentials = st.secrets["gcp_service_account"]
gc = gspread.service_account_from_dict(credentials)
sheet = gc.open("Project-L").sheet1

if 'role' not in st.session_state:
    st.session_state.role = None
    
#CSS------------------------------------------------------------------------------------------------------------------------------
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

st.markdown("""
    <style>
    .stPageLink a {
        display: block;
        text-align: center;
        background-color: grey;
        color: white !important;
        font-size: 50px;
        font-weight: bold;
        padding: 15px;
        border-radius: 10px;
        text-decoration: none !important;
        height: 150px;
        line-height: 50px;
    }
    .stPageLink a:hover {
        background-color: #555555;
    }
    </style>
""", unsafe_allow_html=True)

#Functions--------------------------------------------------------------------------------------------------------------------------------------

def Pop_Up():
    
    st.info("CHOOSE AN OPTION TO ENTER! :D")

    col1, col2, col3 = st.columns(3)
    recruiter = col1.button("RECRUITER",width="stretch")
    guest = col2.button("GUEST", width="stretch")
    friend = col3.button("FRIEND", width="stretch")

    if recruiter:
        st.session_state.role = 'RECRUITER'
        st.rerun()
    elif guest:
        st.session_state.role = 'GUEST'
        st.rerun()
    elif friend:
        st.session_state.role = 'FRIEND'
        st.rerun()

    if st.session_state.role != None: 
        sheet.append_row([datetime.now().strftime("%Y-%m-%d %H:%M:%S"),st.session_state.role])


def Main_Menu():
    st.header("Menu",text_alignment="center")
    st.markdown("Welcome to my page! Here you have a little overview on which pages are available.\nFeel free to discover all of them!",text_alignment='center')
    st.info('Work is currently in progress. Most of the pages are not finished yet.')
  

    col1, col2= st.columns(2)
    with col1:
        st.page_link("About.py",width="stretch")
        st.page_link("Data Analytics.py",width="stretch")
    with col2:
        st.page_link("Application Statistics.py",width="stretch")
        st.button("CV",width="stretch")


if 'role' not in st.session_state or st.session_state.role is None:
    with loading_placeholder:
        with loading_placeholder.spinner("Loading...",show_time=True):
            time.sleep(3)
    Pop_Up()
else:
    Main_Menu()
    