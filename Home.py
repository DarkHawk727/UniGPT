import langchain
import numpy as np
import streamlit as st


def main() -> None:
    st.title("Arjun's Personal AI")
    st.markdown(
        """
    This is a personal AI platform for me. It contains various features:
    * **PDF Interaction**: This is primarily used for homework/assignment help. It works by embedding a PDF to a vectorstore and querying it and then adding that to a custom prompt to a model of choice depending on the question.
    * **Study Sheet Generation**: This feature lets me create studysheets from all the definitions, theorems, corollaries, and other factoids that can be exported to Anki.
    * **Note Transcriber**: Uploading an audio file and using the `whisper` api to transcribe the notes and use another model to convert it to markdown.
    * **Assignment Critiques**: Upload a piece of writing/math/code and have a model offer feedback, can also add an optional assignment description/rubric.
    * **Intelligent Search**: Enhance the intelligent search feature to incorporate natural language understanding capabilities. The platform can analyze your search queries in context and provide more accurate and tailored search results, including relevant articles, research papers, forum discussions, and even suggestions for related concepts.
    * **Text Summarization**: Summarizes documents.
    * **Practice Problem Generator**: Generates practice problems from provided documents of textbooks, assignments, or even topics. Will also provide solutions.
    """
    )

    st.markdown("---")


if __name__ == "__main__":
    main()

# TODO: You should also add a bunch of graphs about stuff like how many tokens youve used, how many times youve used the platform, etc.
