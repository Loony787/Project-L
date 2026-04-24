import streamlit as st
import pandas as pd
import gspread
from datetime import datetime, timedelta
import time

st.set_page_config(layout="wide",initial_sidebar_state="expanded")
st.title("Project: L",text_alignment="center")
st.header("Menu", text_alignment='center')
st.divider()

col1, col2, col3, col4, col5 = st.columns(5)
with col3: 
    loading_placeholder = st.empty()

credentials = st.secrets["gcp_service_account"]
gc = gspread.service_account_from_dict(credentials)
sheet_write = gc.open("Project-L").sheet1

if 'role' not in st.session_state:
    st.session_state.role = None
    
#CSS------------------------------------------------------------------------------------------------------------------------------
st.markdown("""
    <style>
    .stButton button {
        font-size: 50px;
        height: 150px;
        color: white;
        background-color: #b0b0b0;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)
#Functions--------------------------------------------------------------------------------------------------------------------------------------

def Pop_Up():
    col1, col2, col3 = st.columns([1,3,1])
    col2.info("CHOOSE AN OPTION TO ENTER! :D")
    col1, col2, col3, col4, col5 = st.columns(5)
    recruiter = col2.button("RECRUITER",width="stretch")
    guest = col3.button("GUEST", width="stretch")
    friend = col4.button("FRIEND", width="stretch")
    if recruiter:
        st.session_state.role = 'RECRUITER'
    elif guest:
        st.session_state.role = 'GUEST'
    elif friend:
        st.session_state.role = 'FRIEND' 
    if st.session_state.role != None:
        sheet_write.append_row([datetime.now().strftime("%d.%m.%y"),st.session_state.role,datetime.now().strftime("%H:%M:%S")])
        st.rerun()


def Main_Menu():
    col1, col2, col3 = st.columns([1,2,1])
    col2.markdown("Welcome to my page! Here you have a little overview on which pages are available.\nFeel free to discover all of them!",text_alignment='center')
    col2.info('Work in progress... most pages are not finished yet.')
  

    col1, col2, col3, col4= st.columns(4)
    if col2.button('About',width="stretch",):
        st.switch_page('pages/1_About.py')
    if col2.button("Data Analytics",width="stretch"):
        st.switch_page('pages/2_Data Analytics.py')
    if col3.button("Application Statistics",width="stretch"):
        st.switch_page('pages/3_Application Statistics.py')
    col3.button("TBD",width="stretch")


if 'role' not in st.session_state or st.session_state.role is None:
    with loading_placeholder:
        with loading_placeholder.spinner("Loading...",show_time=True):
            time.sleep(3)
    Pop_Up()
else:
    Main_Menu()
    