import streamlit as st
from langchain.document_loaders import PyPDFLoader, DocxLoader

st.title("Assignment Critique")

st.markdown(
    """
    Upload a piece of writing/math/code and have a model offer feedback, can also add an optional assignment description/rubric.
    """
)

assignment_loader = PyPDFLoader()
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


prompt = """
You are a TA for a math and computer science course. You are offering feedback for a student's solution to an assignment before the deadline. Given the following assignment files, followed by the student's solution, suggest improvements to their work. Make sure to explain comments and suggestions well. Do not rewrite the code for them, but instead give plaintext answers. If there, make sure to consider the student's self-assessment of their work.

For code, be sure to focus on the following areas:
- Testing coverage
- Code readability
- Code efficiency
- Code style
- Code structure

For math, be sure to focus on the following areas:
- Mathematical correctness
- Mathematical style
- Proof structure
- Proof clarity

Assignment Text:
{assignment_text}

Student Solution:
{student_solution}

Student Self-Assessment:
{student_self_assessment}
"""