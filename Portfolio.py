import streamlit as st
import pandas as pd
import gspread
from datetime import datetime
import time

#LOAD---------------------------

# if 'starting' not in st.session_state:
    
#     st.session_state.starting = True
# else:
#     st.session_state.starting = True
#REST---------------------------
st.set_page_config(layout="wide",initial_sidebar_state="expanded")
st.title("Project: L",text_alignment="center")
st.divider()

credentials = st.secrets["gcp_service_account"]
gc = gspread.service_account_from_dict(credentials)
sheet = gc.open("Project-L").sheet1

if 'role' not in st.session_state:
    st.session_state.role = None
    
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
    col1, col2, col3 = st.columns(3)
    with col2.spinner("Loading...",show_time=True):
        time.sleep(5)
    Pop_Up()
else:
    Main_Menu()