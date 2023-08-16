import base64

import streamlit as st
from dotenv import load_dotenv
from langchain.callbacks import get_openai_callback
from langchain.chains.question_answering import load_qa_chain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from PyPDF2 import PdfReader

# TODO:
# * Add a preview of the PDF
# * Add the ability to select a PDF from a list of PDFs that have already been uploaded
#


# template = "You are a helpful assistant that allows the user to interact with PDFs, you make use of relevant information"
load_dotenv()

st.title("PDF Chatter")

st.markdown(
    """
    This page lets me chat with an uploaded PDF, ideally the course-notes of a course. It works by embedding all text and storing it inside a vectorstore. Once that has been done, it will be forever saved and you can simply select it again.
    """
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

    text_splitter = CharacterTextSplitter(
        separator=".",
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len,
    )

    chunks = text_splitter.split_text(text)

    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(texts=chunks, embedding=embeddings)

    question = st.text_input("What would you like help with?")
    if question:
        docs = knowledge_base.similarity_search(query=question)

        llm = OpenAI()
        chain = load_qa_chain(llm=llm, chain_type="stuff")

        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=question)
            st.write(f"The cost of this query was {cb}")

        st.write(response)
