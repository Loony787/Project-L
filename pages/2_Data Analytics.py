import pandas as pd
import streamlit as st
import time 

st.set_page_config(layout="wide",initial_sidebar_state="expanded")
def Start():
    if st.session_state.get('role') is None:
        st.switch_page("Portfolio.py")
Start()


col1, col2, col3, col4, col5 = st.columns(5)
with col3.spinner("Loading...",show_time=True):
    time.sleep(1)

st.title("Project: D", text_alignment='center')
st.header("Data Analytics", text_alignment='center')
st.page_link("Portfolio.py", label="Home")
#Content-----------------------------------------------------------------------------------------------------

tab1, tab2, tab3 = st.tabs(["X", "X", "X"])

with tab1:
    st.markdown("Text")

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