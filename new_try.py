import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
from zipfile import ZipFile
import pickle
import numpy as np

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
