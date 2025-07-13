from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate , load_prompt

load_dotenv()
st.header('Research tool')

paper_input = st.selectbox("Select Research paper Name " ,
                        ['Attention is all you need','Diffusion Models Beat GANs on Image Synthesis'])

style_input = st.selectbox("Select Explanation style" , ['Beginner-friendly','Technical'])

length_input = st.selectbox("Select Explanation Length" ,['Short (1-2 paragraph)' , 'Medium (3-4 paragraph)'])



template = load_prompt('template.json')

model = ChatGroq(model_name="llama3-70b-8192",
                api_key="GROQ_API_KEY",
                temperature=0.7)

if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
    'paper_input':paper_input,
    'length_input':length_input,
    'style_input':style_input
    })
    st.write(result.content)

