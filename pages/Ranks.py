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

st.subheader("How does the rank impact the amount of swearing we find?")
col3, col4 = st.columns(2)

songs = pd.read_csv('songs_ranked.csv', index_col = 0)
rank_dta = songs.groupby("rank")['total_swear'].mean()

fig2 = px.line(x=rank_dta.index, y=rank_dta, title="Rank's Impact on Swearing")
# Best Fit Line
slope, intercept = np.polyfit(rank_dta.index, rank_dta.values, 1)
# Calculate fitted values
fit_line = slope * rank_dta.index + intercept

# Add the best fit line as a new trace
fig2.add_trace(go.Scatter(
    x=rank_dta.index,
    y=fit_line,
    mode='lines',
    name='Best Fit Line',
    line=dict(color='red', dash='dash')  # Optional styling: red, dashed line
))

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
	st.write(f'In the chart to the right, there is {percent_change}% more swears on average in the songs that reach ranks 90-100 compared to the ones that make it to 1-10. When looking at the best fit line we can see that the slope is {slope}, meaning that for each rank we drop there is on average that many more swears. Our y-intercept is {intercept}, meaning that songs making it to the number one spot, still have this many swears on average.')

with col4:
	st.plotly_chart(fig2)

st.subheader("What percent of songs at each rank have N number of swear words?")
number = st.number_input(
    "Songs With This Number of Swears", value=1
)

if 'final' in st.session_state:
	
	final = st.session_state['final']
	
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
