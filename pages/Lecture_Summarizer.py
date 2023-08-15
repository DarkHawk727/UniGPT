import streamlit as st
import numpy as np

st.title("Lecture Summarizer")

st.markdown(
    """
    This page lets me summarize documents and create notes from uploaded lecture notes.
    Simply upload a file and the AI will summarize it for you. You can also download a PDF of the rendered markdown.
    """
)

st.file_uploader(
    label="Upload Lecture Files",
    type=["pdf", "docx", "pptx"],
    accept_multiple_files=True,
)

st.markdown("---")
st.markdown(body="## Summarized Notes")

st.button(label="Download PDF")
