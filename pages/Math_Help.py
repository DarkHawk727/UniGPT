import streamlit as st
from dotenv import load_dotenv
from langchain.chains.llm_symbolic_math.base import LLMSymbolicMathChain
from langchain.llms import OpenAI

load_dotenv()

st.title("LLM-assisted Calculations")
st.markdown(
    """
    ## Description

    This page is for specific math help. It uses `sympy` for the symbolic computations. See the *CS_help* page for coding related questions and the *General_PDF_interaction* for other subjects.
    
    ## Usage

    This page is only to be used for calculation questions; this is because the underlying prompt tells the LLM to convert the question into sympy code. Here are some examples of valid and invalid quesions:
    ```
    Question: What is the derivative of x^2?
    Answer: 2*x
    ```
    ```
    Question: Solve the differential equation: y'' - y = e^t
    Answer: Eq(y(t), C2*exp(-t) + C(1+t/2)*exp(t))
    ```
    
    You should NOT ask it math trivia questions, such as:
    ```
    Question: What is the the RREF of a matrix?
    ```
    ```
    Question: What does a derivative represent?
    ```
    For those sorts of questions, either use the general chatbot or [ChatGPT](https://chat.openai.com/).
    
    ---
    """
)

llm = OpenAI(temperature=0)
llm_symbolic_math = LLMSymbolicMathChain.from_llm(llm)

question = st.text_input("Enter your question here:", key="question")

st.markdown("---")
if question:
    answer = llm_symbolic_math.run(question)

    st.header("Response:")
    st.markdown(answer)
