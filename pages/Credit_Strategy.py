import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from codes.login import *
from codes.variables import *
from codes.decay_short_strangle import *


DATA_URL = 'scripmaster-csv-format.csv'

@st.cache(persist=True)
def load_data():
    data = pd.read_csv(DATA_URL)
    return data
df = load_data()

@st.cache(persist=True)
def login_():
    return login()
client = login()

@st.cache(persist=True)
def variables_():
    return variables()
ce,pe,date1,date2 = variables_()

st.sidebar.markdown("### Decay Short Strangle - 1")
CE_strike = st.sidebar.number_input('Enter the CE strike')
PE_strike = st.sidebar.number_input('Enter the PE strike')
if not st.sidebar.checkbox("Hide", True,  key='1'):
    string = '#### ' +  str(CE_strike) + '-CE ' + ' __/__ ' + str(PE_strike) + '-PE'
    st.markdown(string)
    df_ = decay(int(CE_strike) , int(PE_strike), client, ce, pe, date1, date2, df )
    fig, ax = plt.subplots(figsize=(20, 15))
    ax.plot(df_['timestamp'], df_['strangle'], label = 'strangle_value')
    ax.plot(df_['timestamp'], df_['vwap'], label = 'VWAP')
    ax.legend()
    plt.xticks(rotation=45)

    st.pyplot(fig)

st.sidebar.markdown("### Decay Short Strangle - 2")
CE_strike_ = st.sidebar.number_input('Enter the CE strike price')
PE_strike_ = st.sidebar.number_input('Enter the PE strike price')
if not st.sidebar.checkbox("Hide", True, key='2'):
    string_ = '#### ' +  str(CE_strike_) + '-CE ' + ' __/__ ' + str(PE_strike_) + '-PE'
    st.markdown(string_)
    df_ = decay(int(CE_strike_) , int(PE_strike_), client, ce, pe, date1, date2, df )
    fig, ax = plt.subplots(figsize=(20, 15))
    ax.plot(df_['timestamp'], df_['strangle'], label = 'strangle_value')
    ax.plot(df_['timestamp'], df_['vwap'], label = 'VWAP')
    ax.legend()
    plt.xticks(rotation=45)

    st.pyplot(fig)
