import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import seaborn as sb
import matplotlib.pyplot as plt  # needed to close figures
import json
import plotly.express as px


st.subheader("Most Sweary Song Every Year")

@st.cache_data(ttl=None, max_entries=4, show_spinner=False)
def load_most_by_year():
    return pd.read_csv("most_byyear.csv", index_col=0)

@st.cache_data(ttl=None, max_entries=4, show_spinner=False)
def load_which_swear():
    which_swear = pd.read_csv('which_swear.csv', index_col=0)
    return which_swear.reset_index().melt(id_vars="index", var_name="Line", value_name="Value")

@st.cache_data(ttl=None, max_entries=2, show_spinner=False)
def load_traj():
    # traj.json looks like a 2-row structure you index with iloc
    return pd.read_json("traj.json")

data = load_most_by_year()
st.dataframe(data, use_container_width=True)

df_melted = load_which_swear()
# Line plot
fig = px.line(
    df_melted,
    x="index",
    y="Value",
    color="Line",
    title="How Common is Each Swear in Songs OVer Past 4 Decades",
    labels={"index": "X-axis", "Value": "Y-axis"}
)
fig.update_layout(
	xaxis_title="Year",
	yaxis_title="Percent of Songs",
    height = 700,
    width = 900
)
st.plotly_chart(fig)


