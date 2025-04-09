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
	st.subheader("Correlation Matrix of Swears")
	
	corr = final.drop_duplicates(subset = ['title', 'artist'], keep = 'first')[['shit', 'bitch', 'damn', 'dick', 'fuck_total', 'ass', 'hell']]
	corr.corr()
	
	dataplot = sb.heatmap(corr.corr(),vmin = -0.1, vmax = 0.6, annot=True)
	st.pyplot(dataplot.get_figure())
	
	j = pd.read_json('traj.json')
	
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
					ppy.add_trace(go.Scatter(x=x, y=y, mode='lines', name=word))
	
			ppy.update_layout(xaxis=dict(range=[x[0], x[-1]]))
			st.plotly_chart(ppy, use_container_width=True)
	st.subheader("What Percent of the 7 Are Used?")
