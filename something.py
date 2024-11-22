import streamlit as st

st.set_page_config(layout='wide')

import pandas as pd
from zipfile import ZipFile
import pickle
import numpy as np

st.write("Pandas version:", pd.__version__)
st.write("NumPy version:", np.__version__)

# Open the .zip file
with ZipFile('data2.zip', 'r') as f:
    # Extract all contents in the current directory
    f.extractall()

    # Open the .pkl file inside the zip
    with f.open('data2.pkl') as pkl_file:
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


df = pd.concat([data1, data2, data3, data4])



st.subheader("How has swearing in music changed over the past four decades?")
st.write("Andrew Kornder and Goutham Yegappan :)")
st.write(len(df))
