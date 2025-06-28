import streamlit as st
import json

from src.ui.load import LoadStreamlitUI

def load_app():
    """
    Load the Streamlit application.
    """
    
    ui = LoadStreamlitUI()
    user_input = ui.load_ui()

    if not user_input:
        st.error("Failed to load the UI. Please check your configuration.")
        return
    
    if st.session_state.isFetchButtonClicked:
        user_message = st.session_state.timeframe
    
    else:
        user_message = st.text_input("Enter your message:")
        