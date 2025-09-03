import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import seaborn as sb
import matplotlib.pyplot as plt  # needed to close figures
import json

st.subheader("Most Sweary Song Every Year")

@st.cache_data(ttl=None, max_entries=4, show_spinner=False)
def load_most_by_year():
    return pd.read_csv("most_byyear.csv", index_col=0)

@st.cache_data(ttl=None, max_entries=2, show_spinner=False)
def load_traj():
    # traj.json looks like a 2-row structure you index with iloc
    return pd.read_json("traj.json")

data = load_most_by_year()
st.dataframe(data, use_container_width=True)

if "final" in st.session_state:
    final = st.session_state["final"]
    st.subheader("Correlation Matrix of Swears")

    corr_cols = ["shit", "bitch", "damn", "dick", "fuck_total", "ass", "hell"]
    corr_df = (
        final.drop_duplicates(subset=["title", "artist"], keep="first")[corr_cols]
        .corr()
    )

    # Seaborn/Matplotlib → render and CLOSE the figure
    fig, ax = plt.subplots(figsize=(6, 4))
    sb.heatmap(corr_df, vmin=-0.1, vmax=0.6, annot=True, ax=ax)
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)  # <-- IMPORTANT: prevents figure handle leaks

    j = load_traj()
    counts = [j.iloc[1][0], j.iloc[1][1]]
    words = list(j.iloc[0].values)

    with st.container(border=True):
        relative = st.checkbox("Measure by percents instead of absolute counts of swear words")
        on = []
        with st.container():
            for word in words:
                on.append(st.checkbox(word, key=word))

        counts = counts[int(relative)]

        ppy = go.Figure()
        x = list(range(1980, 2024))
        for word, b in zip(words, on):
            if not b:
                continue
            y = counts[word]
            ppy.add_trace(go.Scatter(x=x, y=y, mode="lines", name=word))

        ppy.update_layout(xaxis=dict(range=[x[0], x[-1]]))
        st.plotly_chart(ppy, use_container_width=True)

st.subheader("What Percent of the 7 Are Used?")
