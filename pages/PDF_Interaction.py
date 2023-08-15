import numpy as np
import streamlit as st
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS

# Check if the PDF has already been uploaded to the vectorstore.
# If it has, then query from that.
# If it hasn't, then upload it to the vectorstore and then query from that.


template = "You are a helpful assistant that allows the user to interact with PDFs, you make use of relevant information"

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
    pages = PyPDFLoader(pdf.getvalue()).load_and_split()
    sections = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=100, length_function=len
    ).split_documents(pages)

    faiss_index = FAISS.from_documents(sections, OpenAIEmbeddings())

    retriever = faiss_index.as_retriever()

    memory = ConversationBufferMemory(
        memory_key="chat_history", return_messages=True, output_key="answer"
    )

    chain = ConversationalRetrievalChain.from_llm(
        llm=OpenAI(), retriever=retriever, memory=memory
    )

st.markdown("---")


message = st.chat_message("Assistant")
message.write("Hello human")
message.bar_chart(np.random.randn(30, 3))
