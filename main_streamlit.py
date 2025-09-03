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


# Store values in session state
if 'final' not in st.session_state:
	final = create_data()
	st.session_state['final'] = final

else:
	final = st.session_state['final']

st.set_page_config(layout='wide')


st.subheader("How has swearing in music changed over the past four decades?")
st.write("Andrew Kornder and Goutham Yegappan :)")


st.subheader("Songs Found By Year")

scores = final.groupby('date').count()['title']
fig = px.line(x=scores.index, y=scores)


fig.update_layout(
    title={
        'text': "Songs Found By Week<br><sup>We find more than 90% songs consistently after the 1980's</sup>",
        'y': 0.9,  # Adjust title position
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    width=600,  # Set the chart width
    height=370 
)

# Set axis labels and titles
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="% of Songs Identified",
)

col1, col2 = st.columns(2)
percent_found = round(len(final)/1660, 1) 
percent_found_1980 = round(len(final[final['date'] > '1980'])/(len(final[final['date'] > '1980']['date'].unique()) * 100),3) * 100

with col1:
    st.write("We were able to find ", percent_found, 'of the songs starting from 1960 to the end of 2023. This increases to ', percent_found_1980, "if we start counting songs only from 1980. Depending on when we start counting songs this will change. We were not able to find many songs from the older years because their lyrics were not on Genius. Some of the newer songs were hard to find due to the fact that they are international songs, or that there isn't a clear match that we could find, even if the song was on Genius.")
 
    st.write("The total number of songs is ", len(final))
    st.write("The number of unique songs is ", len(final.drop_duplicates(subset = ['title', 'artist'])))

    st.write("This is ", percent_found, '% identified of the total songs in the charts')


with col2:
    st.plotly_chart(fig)


