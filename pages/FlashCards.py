import base64
from typing import List

import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain.prompts.chat import HumanMessagePromptTemplate, SystemMessage
from pydantic import BaseModel, Field
from PyPDF2 import PdfReader

load_dotenv()


template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                """
Task: Your task is to synthesize mathematical and computer science related definitions, theorems, and corollaries from the given text and condense the information into concise and direct statements using Anki flashcards. Ensure that each statement is clearly written, easily understandable, and adheres to the specified formatting and reference criteria. 

Formatting Criteria: 
- Construct a table with two columns: "Question" and "Answer" delimited by a comma.
- Each entry in the "Question" column should be a question from the given text focusing on definitions, theorems, and algorithms. Make sure to provide any context that might help answering the question.
- The question column should contain the answer to the preceding question.
- Any math should be enclosed by \(\) and be formatted with LaTeX, do not include math inside cloze deletions.

Reference Criteria for each "Flashcard":
- The answer should not exceed 1 sentence.
- Each question-answer pair must be able to stand alone. Include the subject of the question somewhere in the text.
- Keep ONLY simple, direct, cloze deletion statements in the "Question" column.
- End each question-answer pair with a newline


Example: 
Question, Answer 
What is the time complexity of Binary Search, Logarithmic.
What does every finite-dimensional inner product space admit?, An Orthogonal Basis.
"""
            )
        ),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)


st.title("Flashcard Maker 🗃️")
st.markdown(
    """
This page will let you make flashcards from a piece of text or document. Simply paste or upload a document into the given area and the flashcards wil be generated automagically. 
"""
)

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


if subject_name and text:
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)
    output = llm(template.format_messages(text=text))
    df = pd.DataFrame([row.split("?,") for row in output.content.split("\n")])
    st.write(df)
    st.download_button(
        label=f"Download {subject_name}.csv",
        data=df.to_csv(),
        file_name=f"{subject_name}.csv",
        disabled=False,
    )
else:
    st.button(
        label=f"No Text Provided",
        disabled=True,
    )


st.divider()
with st.expander(label="See Prompt"):
    st.text(
        body="""
Task: Your task is to synthesize mathematical and computer science related definitions, theorems, and corollaries from the given text and condense the information into concise and direct statements using Anki flashcards. Ensure that each statement is clearly written, easily understandable, and adheres to the specified formatting and reference criteria. 

Formatting Criteria: 
- Construct a table with two columns: "Question" and "Answer" delimited by a comma.
- Each entry in the "Question" column should be a question from the given text focusing on definitions, theorems, and algorithms. Make sure to provide any context that might help answering the question.
- The question column should contain the answer to the preceding question.
- Any math should be enclosed by \(\) and be formatted with LaTeX, do not include math inside cloze deletions.

Reference Criteria for each "Flashcard":
- The answer should not exceed 1 sentence.
- Each question-answer pair must be able to stand alone. Include the subject of the question somewhere in the text.
- Keep ONLY simple, direct, cloze deletion statements in the "Question" column.
- End each question-answer pair with a newline


Example: 
Question, Answer 
What is the time complexity of Binary Search, Logarithmic.
What does every finite-dimensional inner product space admit?, An Orthogonal Basis.
"""
    )
