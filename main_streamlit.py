import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
from zipfile import ZipFile
import pickle
import numpy as np
import seaborn as sb
import json
import plotly.graph_objects as go

# Open the .zip file

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
st.write("Andrew Kornder and Goutham Yegappan :)")


