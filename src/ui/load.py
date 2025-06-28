import os
import streamlit as st
from datetime import datetime

from langchain_core.messages import AIMessage, HumanMessage
from src.ui.config import LoadConfig

class LoadStreamlitUI:
  def __init__(self):
    self.config = LoadConfig()
    
