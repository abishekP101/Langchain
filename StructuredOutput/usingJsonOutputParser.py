from langchain_groq import ChatGroq
from typing import TypedDict , Annotated , Optional , Literal
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate , load_prompt
from langchain_core.output_parsers import StrOutputParser , JsonOutputParser

model = ChatGroq(
    model_name="llama3-70b-8192",
    api_key="GROQ_API_KEY",
    temperature=0.5)

json = JsonOutputParser()

template = PromptTemplate(
    template='Give me the name , age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': json.get_format_instructions()}
)

chain = template | model | json

result = chain.invoke({})
print(result)