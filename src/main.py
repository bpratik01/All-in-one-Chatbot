import streamlit as st
import json

from src.ui.load import LoadStreamlitUI
from src.llms.groq import GroqLLM


def load_app():
    """
    Load the Streamlit application.
    """
    
    ui = LoadStreamlitUI()
    user_input = ui.load_ui()

    if not user_input:
        st.error("Failed to load the UI. Please check your configuration.")
        return
    
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    
    else:
        user_message = st.text_input("Enter your message:")
        
    if user_message:
        try:
            llm = GroqLLM(user_controls_input=user_input)
            groq_model = llm.get_llm_model()
            
            if not groq_model:
                st.error("Failed to initialize the Groq model. Please check your API key and model selection.")
                return
            
            use_case = user_input.get('use_case')

            if use_case:
                st.error("Error: No usecase selected.")
                return 
        
        except Exception as e:
            raise ValueError(f"An error occurred while processing the input: {e}")
