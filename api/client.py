import requests
import streamlit as st

def get_openai_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/essay/invoke",
            json={'input': {'topic': input_text}},
            timeout=30
        )
        response.raise_for_status()
        return response.json()['output']['content']
    except Exception as e:
        return f"❌ Backend not running: {e}"



def get_ollama_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/poem/invoke",
            json={'input': {'topic': input_text}},
            timeout=30
        )
        response.raise_for_status()
        return response.json()['output']
    except Exception as e:
        return f"❌ Backend not running: {e}"
    

st.title('Langchain Demo With LLAMA2 API')
input_text=st.text_input("Write an essay on")
input_text1=st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response(input_text))
    
if input_text1:
    st.write(get_ollama_response(input_text1))