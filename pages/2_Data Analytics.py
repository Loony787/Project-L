import pandas as pd
import streamlit as st
import gspread
import time 

st.set_page_config(layout="wide",initial_sidebar_state="expanded")
def Start():
    if st.session_state.get('role') is None:
        st.switch_page("Portfolio.py")
Start()

col1, col2, col3, col4, col5 = st.columns(5)
with col3.spinner("Loading...",show_time=True):
    time.sleep(1.5)

st.page_link("Portfolio.py", label="Home")
st.title("Project: D", text_alignment='center')
st.header("Data Analytics", text_alignment='center')
#Visitor Data---------------------------------------------------------------------------------------------------
def Visitor():
    credentials = st.secrets["gcp_service_account"]
    gc = gspread.service_account_from_dict(credentials)
    sheet_read = gc.open("Project-L").sheet1

    data = sheet_read.get_all_records()
    df = pd.DataFrame(data)
    df.columns = ["Date", "Type"]
    st.dataframe(df)
    df_unique = df[['Date', 'Type']].cumsum()
    st.line_chart(df_unique,x='Date', y='count')
#Content-----------------------------------------------------------------------------------------------------

tab1, tab2, tab3 = st.tabs(["Visitors", "X", "X"])

with tab1:
    st.markdown("Text")
    Visitor()
with tab2:
    st.markdown("Text")

with tab3:
    st.markdown("Text")

# st.markdown("Schulden von Gemeinden in Deutschland (pro Einw / in % der Einnahmen)")
# st.markdown("Impact factor von Spielern")#Konstanz, Ballbesitz, Pässe / Passqoute / Tore / Torschüsse / Chancen / Flanken / Pässe ins letzte drittel...
# st.markdown("Tempolimit / Tode durch Geschw. / Umweltkosten / Ölpreise ")
# st.markdown("Nebeneinkünften von Politikern / Parteien / Lobbyverbände")
# st.markdown("Korruption in amerika, wie Pelosi & co. den Markt schlagen")
# st.markdown("")