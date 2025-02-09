if 'final' in st.session_state:
	final = st.session_state['final']
    
    dates = list(final['date'].unique())
    option = st.selectbox(
        "What date would you like data for?",
        tuple(dates),
    )
    
    user_data = final[final['date'] == option] # Filtering the dataframe.
    st.dataframe(user_data)

