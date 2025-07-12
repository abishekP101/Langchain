from langchain.schema import SystemMessage , AIMessage , HumanMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate , load_prompt

model = ChatGroq(model_name="llama3-70b-8192",
                api_key='GROQ_API_KEY',
                temperature=0.5)


messages = [
    SystemMessage(content='You are a helpful assitance'),
    HumanMessage(content='tell me about langchain')
]
result = model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(result)