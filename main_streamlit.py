import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
from zipfile import ZipFile
import seaborn as sb
import json
import plotly.graph_objects as go
import plotly.io as pio

# Open the .zip file
@st.cache_data(ttl=None, max_entries=4, show_spinner=False)
def load_swear_counts():
    return pd.read_csv("counts.csv", index_col=0)

@st.cache_data(ttl=None, max_entries=4, show_spinner=False)
def load_swear_counts_byyear():
    return pd.read_csv("counts_byyear.csv", index_col=0)

@st.cache_data(ttl=None, max_entries=4, show_spinner=False)
def load_raw_swear_counts_byyear():
    return pd.read_csv("rawnumber_byyear.csv", index_col=0)
	
def create_data():
	with ZipFile('data1 (2).zip', 'r') as f:
	    # Extract all contents in the current directory
	    f.extractall()
	
	    # Open the .pkl file inside the zip
	    with f.open('data1.pkl') as pkl_file:
	        # Load the pickle data
	        data1 = pd.read_pickle(pkl_file)
	
	# Open the .zip file
	with ZipFile('data2.zip', 'r') as f:
	    # Extract all contents in the current directory
	    f.extractall()
	
	    # Open the .pkl file inside the zip
	    with f.open('data2.pkl') as pkl_file:
	        # Load the pickle data
	        data2 = pd.read_pickle(pkl_file)
	
	# Open the .zip file
	with ZipFile('data3.zip', 'r') as f:
	    # Extract all contents in the current directory
	    f.extractall()
	
	    # Open the .pkl file inside the zip
	    with f.open('data3.pkl') as pkl_file:
	        # Load the pickle data
	        data3 = pd.read_pickle(pkl_file)
	
	# Open the .zip file
	with ZipFile('data4.zip', 'r') as f:
	    # Extract all contents in the current directory
	    f.extractall()
	
	    # Open the .pkl file inside the zip
	    with f.open('data4.pkl') as pkl_file:
	        # Load the pickle data
	        data4 = pd.read_pickle(pkl_file)


	final = pd.concat([data1, data2, data3, data4])
	final = pd.concat([final.iloc[:,0:6], final.iloc[:,11:]], axis = 1)
	final['fuck_total'] = final['fuck'] + final['motherfuck']
	swears = ["shit", "bitch", "damn", "dick", "fuck_total", "ass", "hell"]
	f = pd.concat([final.iloc[:, :10], final[swears]], axis = 1)
	f['total_swear'] = f.iloc[:, -7:].sum(axis = 1)
	f['percent_swear'] = f['total_swear'] / f['tot_words']

	return f


st.set_page_config(layout='wide')


st.subheader("How has swearing in music changed over the past four decades?")

st.write(f"Our dataset starting in 1980 and ending in 2023 has a total of {"107,294"} songs. Of these there are {"15,020"} unique songs. Of these unique songs, {30.4}% of the songs have atleast one swear in them. Out of all unique songs there are on average {2.54} swears in each song. If we only look at the songs with atleast one swear, then the swear average is {8.37}.")

df = load_swear_counts()
col1, col2 = st.columns(2)
with col1:
	st.table(df)
with col2:
	st.write("In our dataset when looking at the unique songs, the percentages shown on the left indicate how many songs contained that word at least once.")

st.subheader("Distribution of Swears by Decade")

option = st.selectbox(
    "Do you want the raw number or percentage of songs with swears by decade?",
    ("Percentage", "Raw"),
)

if option == "Percentage":
	data = load_swear_counts_byyear()
	st.table(data)
else:
	data = load_raw_swear_counts_byyear()
	st.table(data)

# Load figure from JSON file
with open("swears_bydecade.json", "r") as f:
    fig = pio.from_json(f.read())
st.plotly_chart(fig)



