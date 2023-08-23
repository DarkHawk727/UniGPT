# Personal AI

This is a collection of LLM-powered tools that I have developed for personal use.

* **PDF Interaction**: This is primarily used for homework/assignment help. It works by embedding a PDF to a vectorstore and querying it and then adding that to a custom prompt to a model of choice depending on the question. I can also ask the LLM to compile all the theorems, definitions, and corollaries.
* **Note Transcriber**: Uploading an audio file and using the `whisper` api to transcribe the notes and use another model to convert it to markdown.
* **Assignment Critiques**: Upload a piece of writing/math/code and have a model offer feedback, can also add an optional assignment description/rubric.
* **Intelligent Search**: Enhance the intelligent search feature to incorporate natural language understanding capabilities. The platform can analyze your search queries in context and provide more accurate and tailored search results, including relevant articles, research papers, forum discussions, and even suggestions for related concepts.
* **Text Summarization**: Summarizes documents.
* **Practice Problem Generator**: Generates practice problems from provided documents of textbooks, assignments, or even topics. Will also provide solutions.
* **Flashcard Generation**: Upload some text and generate a `.csv` containing flashcards that can be exported to Anki.

## Current Issues

* `FlashCards.py`: Currently does not incorporate the input text and instead generates more from just the prompt.
* `General_PDF_interaction.py`: Does not have a selector for previously uploaded documents using chromadb.

## Sources

* https://github.com/oresttokovenko/gpt-anki/blob/main/src/generate_deck.py for the flascards