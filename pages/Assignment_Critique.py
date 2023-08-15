import streamlit as st

st.title("Assignment Critique")

st.markdown(
    """
    Upload a piece of writing/math/code and have a model offer feedback, can also add an optional assignment description/rubric.
    """
)
st.file_uploader(
    label="Upload Assignment Files",
    type=["pdf", "docx", ".py", ".md"],
    accept_multiple_files=True,
)

additional_docs = st.radio(
    label="Rubric / Marking Scheme",
    options=("Rubric", "Assginment Description", "Enter Text"),
)

if additional_docs == "Enter Text":
    additional_text = st.text_input(
        label="Enter things you want the AI to focus on when critiquing:",
        max_chars=1000,
    )
else:
    st.file_uploader(
        label="Upload Assignment Description/Rubric Files",
        type=["pdf", "docx", ".py", ".md"],
        accept_multiple_files=True,
    )

st.markdown("---")
st.subheader("Feedback:")

if additional_docs == "Enter Text":
    st.text(f"The additional text your provided was: {additional_text}")
