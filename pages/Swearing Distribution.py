import plotly.graph_objects as go
from plotly.subplots import make_subplots
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


st.subheader("Trajectory of Swearing in Music Over Time Raw Value")

if 'final' in st.session_state:
	final = st.session_state['final']
    
	numb = st.number_input("Songs With This # of Swears", value=1)
	num_swears = final[final['total_swear'] >= numb].groupby('date').count()['title']/final.groupby('date').count()['title']
	num_swears = num_swears.fillna(0)
	fig5 = px.line(x=num_swears.index, y=num_swears, title="Rank's Impact on Swearing")
	st.plotly_chart(fig5)
	
	st.subheader("Distribution of Songs")
	
	
	# Create a 3x2 subplot layout and specify subplot titles dynamically
	years = list(range(1960, 2020, 10))
	titles = [f"{year} - {year + 9}" for year in years]  # Titles for each subplot
	fig = make_subplots(rows=3, cols=2, subplot_titles=titles)
	
	# Initialize row and column for subplots
	row = 1
	col = 1
	
	# Iterate through the years and add each bar plot as a subplot
	for year in years:
		print(year)
		
		# Filter data by year range
		dta = final[(final['date'] > str(year)) & (final['date'] < str(year + 10))]
		
		# Calculate percentage
		percent = dta.groupby('total_swear').count().iloc[1:, :] / len(dta)
		
		# Create the bar plot
		bar_data = go.Bar(x=percent.index, y=percent['title'], showlegend=False)
		
		# Add the bar plot to the subplot figure
		fig.add_trace(bar_data, row=row, col=col)
		
		# Update layout for each subplot's axes
		fig.update_yaxes(range=[0, 0.1], row=row, col=col)
		fig.update_xaxes(range=[0, 50], row=row, col=col)
		
		# Move to the next subplot position
		col += 1
		if col > 2:
		    col = 1
		    row += 1
	
	
	# Update the overall layout (no legend)
	fig.update_layout(height=900, width=1000, title_text="Swear Word Frequency by Year Range", showlegend=False)
	
	st.plotly_chart(fig)

'''
data = pd.read_csv('percent_dist.csv', index_col = 0)
data.columns = data.columns.astype(float)
st.subheader("Trajectory of Swearing in Music Over Time")
number = st.number_input(
    "Songs With This Percent of Swears", value=0.01, min_value = 0.01, max_value = 0.9
)
num_swears = data[number]
fig4 = px.line(x=num_swears.index, y=num_swears, title="Rank's Impact on Swearing")
st.plotly_chart(fig4)
'''
