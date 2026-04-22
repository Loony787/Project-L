import pandas as pd
import streamlit as st
import gspread

#Website------------------------------------------------------------------------------------------------------------------------
st.set_page_config(layout="wide",initial_sidebar_state="expanded")
st.page_link("Portfolio.py", label="Home")

if st.session_state.get('role') is None:
    st.switch_page("Portfolio.py")

st.title("Project: J",text_alignment='center')
st.header("Application statistics", text_alignment='center')

#Import--------------------------------------------------------------------------------------------------------------------------

credentials = st.secrets["gcp_service_account"]
gc = gspread.service_account_from_dict(credentials)
sheet = gc.open("Project-J").sheet1

#Basic preparations--------------------------------------------------------------------------------------------------------------

data = sheet.get_all_records()
df = pd.DataFrame(data)
df = df.iloc[:,0].str.split(";", expand=True)
df.columns = ["Company", "Status", "Rating", "Location", "Application Month", "IDC1", "IDC2", "IDC3", "IDC4", "IDC5", "IDC6"]
df.index = range(1, len(df)+1)
df.index.name = "No."
df = df[df.iloc[:, 0] != ""]
df['Status']= df['Status'].replace({
    'GameIsGone': 'No Answer'})
#st.dataframe(df)

#Next Step-------------------------------------------------------------------------------------------------------------------------
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
def BarChart():
    df_Unique = df[["Status","Application Month"]].value_counts().reset_index()
    #st.dataframe(df_Unique)
    df_Unique["Application Month"] = pd.Categorical(df_Unique["Application Month"], categories= month_order, ordered=True)
    st.bar_chart(df_Unique,x='Application Month',y='count',color='Status')

#Metrics---------------------------------------------------------------------------------------------------------

OA_Value = df[df["Status"] == "Pending"].shape[0]
RA_Value = df[df["Status"] == "Rejected"].shape[0]
NAE_Value = df[df["Status"] == "No Answer"].shape[0]
INT_Value = df[df["Status"] == "Interviewed"].shape[0]
OFF_Value = df[df["Status"] == "Offer"].shape[0]
TA_Value = OA_Value + RA_Value + NAE_Value + INT_Value + OFF_Value

OA_Delta = f"{round(OA_Value / TA_Value * 100, 2)}%"
RA_Delta = f"{round(RA_Value / TA_Value * 100, 2)}%"
NAE_Delta = f"{round(NAE_Value / TA_Value * 100, 2)}%"
INT_Delta = f"{round(INT_Value / TA_Value * 100, 2)}%"
OFF_Delta = f"{round(OFF_Value / TA_Value * 100, 2)}%"

def Absolute_METRICS():
    col1, col2, col3= st.columns(3)
    col1.metric(label= 'Total Applications', value= TA_Value, delta="-%", delta_color='violet', delta_arrow='off')
    col2.metric(label= 'Open Applications', value= OA_Value, delta=OA_Delta, delta_color='violet', delta_arrow='off')
    col3.metric(label= 'Rejected Applications', value= RA_Value, delta=RA_Delta, delta_color='violet', delta_arrow='off')
    col1.metric(label= 'Interviews', value= INT_Value, delta= INT_Delta, delta_color='violet', delta_arrow='off')
    col2.metric(label= 'Offers', value=OFF_Value, delta=OFF_Delta, delta_color='violet', delta_arrow='off')
    col3.metric(label= 'No Answer Expected', value= NAE_Value, delta=NAE_Delta, delta_description='*Application was 2 Months ago', delta_color='violet', delta_arrow='off')

#RUN-----------------------------------------------------------------------------------------------------------------
st.divider()
Absolute_METRICS()
st.divider()
BarChart()
st.divider()