from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


import os
os.environ["OPENAI_API_KEY"]= ""

# prompt template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful AI assistant. Answer the user's questions clearly and accurately."
    ),
    (
        "human",
        "{question}"
    )
])

# openAI llm
llm= ChatOpenAI(model="gpt-5.4-mini", temperature=1)
output_parser= StrOutputParser()
chain= prompt|llm|output_parser

response= chain.invoke("ask me anything: what is different between generative ai and agentic ai")
print(response)