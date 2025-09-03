import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

st.subheader("Trajectory of Swearing in Music Over Time Raw Value")

@st.cache_data(ttl=None, max_entries=3, show_spinner=False)
def load_dist_figure():
    with open("dist_figure.json", "r") as f:
        return pio.from_json(f.read())  # cached figure object

@st.cache_data(ttl=None, max_entries=3, show_spinner=False)
def load_percent_dist():
    df = pd.read_csv("percent_dist.csv", index_col=0)
    df.columns = df.columns.astype(float)
    return df

@st.cache_data(ttl=None, max_entries=3, show_spinner=False)
def load_songs_by_swears():
    df = pd.read_csv("songs_by_swears.csv", index_col=0)
    # columns are numeric counts; keep as int if possible
    try:
        df.columns = df.columns.astype(int)
    except Exception:
        pass
    return df

# 1) Cached JSON figure
fig_raw = load_dist_figure()
st.plotly_chart(fig_raw, use_container_width=True)

# 2) Percent threshold chart
st.subheader("Trajectory of Swearing in Music Over Time")
percent_df = load_percent_dist()
percent = st.number_input("Songs With This Percent of Swears", value=0.01, min_value=0.01, max_value=0.9)
if float(percent) in percent_df.columns:
    s = percent_df[float(percent)]
    fig_pct = px.line(x=s.index, y=s, title="Percent threshold over time")
    st.plotly_chart(fig_pct, use_container_width=True)
else:
    st.info("No data for that percent threshold.")

# 3) By absolute count chart
count_df = load_songs_by_swears()
count = st.number_input("Songs With This # of Swears", value=1, min_value=0, max_value=int(count_df.columns.max()))
if int(count) in count_df.columns:
    s2 = count_df[int(count)]
    fig_cnt = px.line(x=s2.index, y=s2, title="Count threshold over time")
    st.plotly_chart(fig_cnt, use_container_width=True)
else:
    st.info("No data for that count.")
