import pandas as pd
import streamlit as st
st.set_page_config(layout="wide",initial_sidebar_state="expanded")
st.page_link("Portfolio.py", label="Home")

if st.session_state.get('role') is None:
    st.switch_page("Portfolio.py")

st.title("Data Analytics")

tab1, tab2, tab3 = st.tabs(["Correlations", "InvestmentEvaluations", "Papers / Articles / Studies"])

with tab1:
    st.markdown("Text")

with tab2:
    st.markdown("Text")

with tab3:
    st.markdown("Text")

st.markdown("Schulden von Gemeinden in Deutschland (pro Einw / in % der Einnahmen)")
st.markdown("Impact factor von Spielern")#Konstanz, Ballbesitz, Pässe / Passqoute / Tore / Torschüsse / Chancen / Flanken / Pässe ins letzte drittel...
st.markdown("Tempolimit / Tode durch Geschw. / Umweltkosten / Ölpreise ")
st.markdown("Nebeneinkünften von Politikern / Parteien / Lobbyverbände")
st.markdown("Korruption in amerika, wie Pelosi & co. den Markt schlagen")
st.markdown("")