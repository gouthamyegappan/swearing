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

if 'final' in st.session_state:
	final = st.session_state['final']
    
	dates = list(final['date'].unique())
	option = st.selectbox(
	"What date would you like data for?",
	tuple(dates),
	)
	
	user_data = final[final['date'] == option] # Filtering the dataframe.
	st.dataframe(user_data)

