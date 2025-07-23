from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langserve import add_routes

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY1')

generic_prompt = 'Translate the following into {language}'
prompt = ChatPromptTemplate.from_messages(
    [('system' , generic_prompt),
     ('user' , "{text}")]
)
llm = ChatGroq(model='Gemma2-9b-It' , groq_api_key=GROQ_API_KEY)

parser = StrOutputParser()
chain = prompt | llm | parser


app = FastAPI(title="langchain server" , version="1.0" , description='A simple API server using Langchain runnable sequence')

add_routes(
    app,
    chain,
    path='/chain'
)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host='localhost' , port=8000)