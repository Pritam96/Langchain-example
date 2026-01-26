from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
import streamlit as st
import os

from dotenv import load_dotenv

load_dotenv()


# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("LangChain Demo with LLAMA2")
input_text = st.text_input("Search the topic you want")

# LLM
llm = OllamaLLM(model="llama2-uncensored")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    try:
        st.write(chain.invoke({"question": input_text}))
    except Exception as e:
        st.error(str(e))
