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
credentials = st.secrets["gcp_service_account"]
gc = gspread.service_account_from_dict(credentials)
sheet_read = gc.open("Project-L").sheet1

data = sheet_read.get_all_records()
df = pd.DataFrame(data)
df.columns = ["Date", "Type", "Time"]

RECRUITER_VALUE = df[df['Type'] == 'RECRUITER'].shape[0]
GUEST_VALUE = df[df['Type'] == 'GUEST'].shape[0]
FRIEND_VALUE = df[df['Type'] == 'FRIEND'].shape[0]
TV_VALUE = RECRUITER_VALUE + GUEST_VALUE + FRIEND_VALUE

RECRUIT_DELTA = f"{round(RECRUITER_VALUE / TV_VALUE * 100, 2)}%"
GUEST_DELTA = f"{round(GUEST_VALUE / TV_VALUE* 100, 2)}%"
FRIEND_DELTA = f"{round(FRIEND_VALUE/ TV_VALUE * 100, 2)}%"

def VISITS():
    col1, col2, col3, col4, col5 = st.columns([0.5, 1, 1, 1, 1])
    col2.metric(label='Total Visits', value=TV_VALUE,delta='-%',delta_color='violet', delta_arrow='off')
    col3.metric(label='Recruiter Visits', value= RECRUITER_VALUE, delta=RECRUIT_DELTA, delta_color='violet', delta_arrow='off')
    col4.metric(label='Guest Visits', value= GUEST_VALUE, delta=GUEST_DELTA, delta_color='violet', delta_arrow='off')
    col5.metric(label='Friend Visits', value=FRIEND_VALUE, delta=FRIEND_DELTA, delta_color='violet', delta_arrow='off')
    
    df['Date']= pd.to_datetime(df["Date"], format="%d.%m.%y")
    df_sort = df.sort_values(by='Date')
    st.dataframe(df_sort)
    df_group = df_sort.groupby('Date').size().reset_index(name='Visits')
    df_group['Date']= pd.to_datetime(df["Date"], format="%d.%m.%y")
    st.dataframe(df_group)

    df_group['Visits']= df_group['Visits'].cumsum()
    st.line_chart(df_group,x='Date', y='Visits')
    
    
#Content-----------------------------------------------------------------------------------------------------

tab1, tab2, tab3 = st.tabs(["Visits", "X", "X"])

with tab1:
    VISITS()
    #Reset button for charts?!
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