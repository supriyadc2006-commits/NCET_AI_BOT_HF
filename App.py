import streamlit as st
from transformers  import pipeline

#Load the summarization model
@st.cache_resource
def load_summarizer():
  return pipeline("summarization",model="sshleifer/distilbart-cnn-12-6")
