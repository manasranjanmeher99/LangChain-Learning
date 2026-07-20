from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os

# API Keys
os.environ["OPENAI_API_KEY"] = ""
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMIT_API_KEY"] = ""

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful chatbot. Please answer the user's questions clearly."),
    ("human", "{question}")
])

# Streamlit UI
st.title("LLM-OPENAI PROJECT - CUSTOM GPT-5 BY manas")

input_text = st.text_input("How may I help you?")

# LLM
llm = ChatOpenAI(
    model="gpt-5.4-mini",
    temperature=1
)

output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))