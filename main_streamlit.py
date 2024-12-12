import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
from zipfile import ZipFile
import pickle
import numpy as np
import seaborn as sb

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


st.subheader("Trajectory of Swearing in Music Over Time Raw Value")
numb = st.number_input(
    "Songs With This # of Swears", value=1)
num_swears = final[final['total_swear'] >= numb].groupby('date').count()['title']/final.groupby('date').count()['title']
num_swears = num_swears.fillna(0)
fig5 = px.line(x=num_swears.index, y=num_swears, title="Rank's Impact on Swearing")
st.plotly_chart(fig5)

st.subheader("Distribution of Songs")
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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

st.subheader("Correlation Matrix of Swears")

final['fuck_total'] = final['fuck'] + final['motherfuck']
corr = final.drop_duplicates(subset = ['title', 'artist'], keep = 'first')[['shit', 'bitch', 'damn', 'dick', 'fuck_total', 'ass', 'hell']]
corr.corr()

dataplot = sb.heatmap(corr.corr(),vmin = -0.1, vmax = 0.6, annot=True)
st.pyplot(dataplot.get_figure())


dates = list(final['date'].unique())
option = st.selectbox(
    "What date would you like data for?",
    tuple(dates),
)
user_data = final[final['Years'] == option] # Filtering the dataframe.
st.dataframe(user_data.head(5))

st.subheader("What Percent of the 7 Are Used?")
