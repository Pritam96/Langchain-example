from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv

# Load env vars
load_dotenv()

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("LangChain Demo with OpenAI")
input_text = st.text_input("Search the topic you want")

# LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    try:
        st.write(chain.invoke({"question": input_text}))
    except Exception as e:
        st.error(str(e))
