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

final = st.session_state['final']
st.write(f'{len(final)} is the length of the data')
