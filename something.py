import streamlit as st

st.set_page_config(layout='wide')

import pandas as pd
from zipfile import ZipFile
import pickle

dta = pd.read_csv('Genius_Lyrics.csv')
st.write(dta.iloc[0])
'''
# Open the .zip file
with ZipFile('data1.zip', 'r') as f:
    # Extract all contents in the current directory
    f.extractall()

    # Open the .pkl file inside the zip
    with f.open('data1.pkl') as pkl_file:
        # Load the pickle data
        data = pickle.load(pkl_file)

# Check if the data is already a DataFrame
if isinstance(data, pd.DataFrame):
    df = data
else:
    # If not a DataFrame, attempt to convert
    df = pd.DataFrame(data)

# Display the DataFrame
'''


st.subheader("How has swearing in music changed over the past four decades?")
st.write("Andrew Kornder and Goutham Yegappan :)")
st.write(len(df))
