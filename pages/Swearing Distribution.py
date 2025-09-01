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
import plotly.io as pio

st.subheader("Trajectory of Swearing in Music Over Time Raw Value")

# Read the JSON file and convert it back to a Plotly figure
with open("dist_figure.json", "r") as f:
    fig_json = f.read()

# Load the figure from the JSON string
fig = pio.from_json(fig_json)
st.plotly_chart(fig)

data = pd.read_csv('percent_dist.csv', index_col = 0)
data.columns = data.columns.astype(float)
st.subheader("Trajectory of Swearing in Music Over Time")
number = st.number_input(
    "Songs With This Percent of Swears", value=0.01, min_value = 0.01, max_value = 0.9
)
num_swears = data[number]
fig4 = px.line(x=num_swears.index, y=num_swears, title="Songs with this percent of swears")
st.plotly_chart(fig4)


data2 = pd.read_csv('songs_by_swears.csv', index_col = 0)
numb2 = st.number_input("Songs With This # of Swears", value=1, max_value = 30)
data2.columns = data2.columns.astype(float)
num_swears2 = data2[numb2]
fig5 = px.line(x=num_swears2.index, y=num_swears2, title="Songs with this number of swears")
st.plotly_chart(fig5)

