import base64

import streamlit as st
from dotenv import load_dotenv
from langchain.callbacks import get_openai_callback
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader

load_dotenv()

st.title("Flashcard Maker 🗃️")
st.markdown(
    """
This page will let you make flashcards from a piece of text or document. Simply paste or upload a document into the given area and the flashcards wil be generated automagically. 
"""
)

prompt = """
Review Text: "Source text"

Task: Your task is to synthesize mathematical and computer science related definitions, theorems, and corollaries from the given text and condense the information into concise and direct statements using Anki cloze deletion mark-up. Ensure that each statement is clearly written, easily understandable, and adheres to the specified formatting and reference criteria. 

Formatting Criteria: 
- Construct a table with two columns: "Statements" and "Number".
- Each row of the "Statements" column should contain a single statement written in Anki cloze deletion mark-up, focusing on definitions, theorems, and algorithms.
- The "Number" column should serve to number each row, facilitating feedback.
- Any math should be enclosed by \(\) and be formatted with LaTeX, do not include math inside cloze deletions.

Reference Criteria for each "Statement":
- Restrict each statement to 2 cloze deletions. If needed, you may add 1-2 more cloze deletions but restrict them to either cloze1 or cloze2.
- Limit the word count of each statement to less than 40 words.
- Keep the text within the cloze deletions limited to one or two key words.
- Each statement must be able to stand alone. Include the subject of the statement somewhere in the text.
- Keep ONLY simple, direct, cloze deletion statements in the "Statements" column.

Example: 
| Statements | Number |
| --- | --- |
| {{c1::O(log(n))}} is is the time complexity of Binary Search. | 1 |
| Every finite-dimensional inner product space admits an {{c1::orthogonal basis}}. | 2 |
"""

st.divider()
st.subheader(body="Input Area")

subject_name = st.text_input(
    label="Enter subject/class name:",
)
text = st.text_area(
    label="Enter the text",
)

pdf = st.file_uploader(
    label="Upload Lecture Files",
    type=["pdf"],
    accept_multiple_files=False,
)

if pdf is not None:
    base64_pdf = base64.b64encode(pdf.read()).decode("utf-8")
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)

    pdf_reader = PdfReader(pdf)
    text = "".join([page.extract_text() for page in pdf_reader.pages])

st.divider()

text_splitter = CharacterTextSplitter(
    separator=".",
    chunk_size=1000,
    chunk_overlap=100,
    length_function=len,
)
st.write(text)

st.subheader(body="Output")

# TODO: Make this work using langchain lmao.
llm = OpenAI(temperature=0, model_name="gpt-4")


flashcards = ""

if subject_name:
    st.download_button(
        label=f"Download Flashcards for {subject_name}",
        data=flashcards,
        file_name=f"{subject_name}.csv",
        disabled=False,
    )
else:
    st.download_button(
        label=f"Download Flashcards for {subject_name}",
        data=flashcards,
        file_name=f"{subject_name}.csv",
        disabled=True,
    )


st.divider()
with st.expander(label="See Prompt"):
    st.text(body=prompt)
