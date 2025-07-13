from langchain_groq import ChatGroq
from typing import TypedDict , Annotated , Optional , Literal
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate , load_prompt
from langchain_core.output_parsers import StrOutputParser

model = ChatGroq(
    model_name="llama3-70b-8192",
    api_key="GROQ_API_KEY",
    temperature=0.5)


template = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)
prompt1 = template.invoke({'topic':'Apple'})
result = model.invoke(prompt1)

template2 = PromptTemplate(
    template='create a 5 line summary of the {content} in five points',
    input_variables=['content']
)

parser = StrOutputParser()


chain = template | model | parser | template2 | model | parser