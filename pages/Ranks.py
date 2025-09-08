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

st.set_page_config(layout='wide')

st.subheader("How does the rank impact the amount of swearing we find?")
col3, col4 = st.columns(2)

songs = pd.read_csv('rank_impact_on_swearing.csv', index_col = 0)
def get_rank_graph(col, title, yaxis):
    rank_dta = songs.groupby("rank")[col].mean()
    
    fig2 = px.line(x=rank_dta.index, y=rank_dta, title= title)
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
            'text': "Rank's Impact on Swearing",
            'y': 0.9,  # Adjust title position
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        width=600,  # Set the chart width
        height=370 
    )
    
    fig2.update_layout(
        xaxis_title="Rank",
        yaxis_title=yaxis
    )
    
    old = rank_dta[:10].sum()/10
    new = rank_dta[-10:].sum()/10
    percent_change = round((new-old)/old, 3) * 100

    return fig2, old, new, percent_change, slope

fig2, old2, new2, percent_change2, slope2 = get_rank_graph('total_swear', "Rank's Impact on Average Number of Swears in a Song", "Average Number of Swears")
fig3, old3, new3, percent_change3, slope3 = get_rank_graph('percent_swear', "Rank's Impact on Percentage of Swears in a Song", "Percent of Swears")

st.write(f'The two charts below illustrate the relationship between a song’s rank and the prevalence of swearing in its lyrics. The chart on the left depicts the average number of swears per song, while the chart on the right reports the average percentage of words classified as swears. Both figures indicate a positive association between rank and the likelihood of swearing. In the left chart, the slope is {round(slope2, 2)}, suggesting that for each unit decrease in rank, the expected number of swears increases by approximately {round(slope2, 2)}.'
)

with col3:
	st.plotly_chart(fig2)

with col4:
	st.plotly_chart(fig3)

st.subheader("What percent of songs at each rank have N number of swear words?")
number = st.selectbox(
    "How many swears would you like to filter for?",
    ("1", "3", "5", "10", "15", "20"),
)

data = pd.read_csv('swear_words_by_rank.csv', index_col = 0)
data.columns = data.columns.astype(int)
num_swears = data[int(number)]
fig3 = px.line(x=num_swears.index, y=num_swears, title="Rank's Impact on Swearing")
fig3.update_layout(
	xaxis_title="Rank",
	yaxis_title="Percent of Songs"
)

st.write(f'The chart below shows the percentage of songs at each rank that contain at least the number of swears specified above.')
st.plotly_chart(fig3)

	
