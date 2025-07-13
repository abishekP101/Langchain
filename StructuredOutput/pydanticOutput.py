from langchain_groq import ChatGroq
from typing import TypedDict , Annotated , Optional , Literal
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser , JsonOutputParser
from langchain.output_parsers import StructuredOutputParser , ResponseSchema
from langchain.output_parsers import OutputFixingParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field

model = ChatGroq(
    model_name="llama3-70b-8192",
    api_key="FROQ_API_KEY",
    temperature=0.5)

class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(gt=18 , description='Age of a person')
    city: str = Field(description='name of the city where the person belongs to')

parser  = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name , age , city of a fictional {place} person \n{format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt = template.invoke({'place':'Indian'})

result = model.invoke(prompt)

final_res = parser.parse(result.content)

print(final_res)
