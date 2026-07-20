from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


import streamlit as st
import os
os.environ["OPENAI_API_KEY"] = "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"
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","I am chatbot. I am here to assist you. Please type your queries"),
        ("user","Question:{Question}")

    ]

)


# streamlit framework

st.title = ('LLM-OPENAI PROJECT - CUSTOM GPT-5 BY SITU')
input_text = st.text_input("How may i help your")


# openai llm

llm = ChatOpenAI(
    model="gpt-5.4-mini",
    temperature=1
)
output_parser = StrOutputParser()
chain = prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'Question'}))

