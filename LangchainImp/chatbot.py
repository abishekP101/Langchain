from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate , load_prompt

model = ChatGroq(model_name="llama3-70b-8192",
                api_key="GROQ_API_KEY",
                temperature=0.5)
history = []

while True:
    user_input = input('You:  ')
    history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(history)
    history.append(result.content)

    print("AI: " ,result.content)


