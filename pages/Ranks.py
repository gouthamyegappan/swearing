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

final = st.session_state['final']
st.write(f'{len(final)} is the length of the data')

st.subheader("How does the rank impact the amount of swearing we find?")
col3, col4 = st.columns(2)

songs = pd.read_csv('songs_ranked.csv', index_col = 0)
rank_dta = songs.groupby("rank")['total_swear'].mean()

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


num_swears = final[final['total_swear'] >= number].groupby('rank').count()['title']/final.groupby('rank').count()['title']
fig3 = px.line(x=num_swears.index, y=num_swears, title="Rank's Impact on Swearing")
st.plotly_chart(fig3)


st.subheader("Trajectory of Swearing in Music Over Time")
number = st.number_input(
    "Songs With This Percent of Swears", value=0.01, min_value = 0.001, max_value = 0.9
)
num_swears = final[final['percent_swear'] >= number].groupby('date').count()['title']/final.groupby('date').count()['title']
num_swears = num_swears.fillna(0)
fig4 = px.line(x=num_swears.index, y=num_swears, title="Rank's Impact on Swearing")
st.plotly_chart(fig4)
