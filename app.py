import streamlit as st
from utils.model_loader import load_summarizer


st.set_page_config(page_title="Multi Summarizer")

st.title("Summarizer")

summarizer = load_summarizer()

text = st.text_area("Sample text")

if st.button("summarize"):
    if text.strip():
        with st.spinner("Summarizing....."):
            summary = summarizer(text,max_length = 100, min_length= 25,do_sample=False)[0]['summary_text']
        st.subheader("Summary")
        st.success(summary)
    else:
        st.warning("Paste some test") 
