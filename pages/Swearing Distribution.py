import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

st.subheader("Trajectory of Swearing in Music Over Time Raw Value")
@st.cache_data(ttl=None, max_entries=3, show_spinner=False)
def load_percent_dist():
    df = pd.read_csv("percent_dist.csv", index_col=0)
    return df

# 2) Percent threshold chart
st.subheader("Trajectory of Swearing in Music Over Time")
percent_df = load_percent_dist()

num = st.selectbox(
    "Number of Swears",
    ("1", "2", "5", "10"),
)
s = percent_df[num]
fig_pct = px.line(x=s.index, y=s, title=f"Percent of Songs with {num} number of swears")
st.plotly_chart(fig_pct, use_container_width=True)


