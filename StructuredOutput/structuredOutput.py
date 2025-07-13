from langchain_groq import ChatGroq
from typing import TypedDict , Annotated , Optional , Literal
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser , JsonOutputParser
from langchain.output_parsers import StructuredOutputParser , ResponseSchema
from langchain.output_parsers import OutputFixingParser


model = ChatGroq(
    model_name="llama3-70b-8192",
    api_key="GROQ_API_KEY",
    temperature=0.5)

schema = [
    ResponseSchema(name='fact_1' , description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2' , description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3' , description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)
fixing_parser = OutputFixingParser.from_parser(parser)

template = PromptTemplate(
    template='Give me 3 facts about {topic} \n{format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
chain = template | model | parser

result = chain.invoke({'topic':'Black hole'})
print(result)



