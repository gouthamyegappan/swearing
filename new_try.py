import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
from zipfile import ZipFile
import pickle
import numpy as np

# Open the .zip file
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

col1, col2 = st.columns(2)
percent_found = round(len(final)/1660, 1) 
percent_found_1980 = round(len(final[final['date'] > '1980'])/(len(final[final['date'] > '1980']['date'].unique()) * 100),3) * 100

with col1:
    st.write("We were able to find ", percent_found, 'of the songs starting from 1960 to the end of 2023. This increases to ', percent_found_1980, "if we start counting songs only from 1980. Depending on when we start counting songs this will change. We were not able to find many songs from the older years because their lyrics were not on Genius. Some of the newer songs were hard to find due to the fact that they are international songs, or that there isn't a clear match that we could find, even if the song was on Genius.")
 
    st.write("The total number of songs is ", len(final))
    st.write("The number of unique songs is ", len(final.drop_duplicates(subset = ['title', 'artist'])))

    st.write("This is ", percent_found, 'of the total songs')


with col2:
    st.plotly_chart(fig)

'''
st.subheader("How does the rank impact the amount of swearing we find?")
col3, col4 = st.columns(2)

songs = pd.read_csv('songs_ranked.csv', index_col = 0)
rank_dta = songs.groupby("rank").mean()['total_swear']

fig2 = px.line(x=rank_dta.index, y=rank_dta, title="Rank's Impact on Swearing")
fig2.update_layout(
    title={
        'text': "Rank's Impact on Swearing<br><sup>There seems to be a relationship between rank and number of swears</sup>",
        'y': 0.9,  # Adjust title position
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    width=600,  # Set the chart width
    height=370 
)

old = rank_dta[:10].sum()/10
new = rank_dta[-10:].sum()/10
percent_change = round((new-old)/old, 3) * 100

with col3:
	st.write('In the chart to the right, there is a ', percent_change, "% more total number of swears on average out of the bottom 10 songs vs the top 10")

with col4:
	st.plotly_chart(fig2)


st.subheader("What percent of songs at each rank have N number of swear words?")
number = st.number_input(
    "Songs With This Number of Swears", value=1
)
