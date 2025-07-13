from langchain_groq import ChatGroq
from typing import TypedDict , Annotated , Optional , Literal
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate , load_prompt
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel , RunnableBranch , RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from typing import Literal


class Feedback(BaseModel):
    sentiment: Literal['positive' , 'negative'] = Field(description='give the sentiment of the feedback')


parser2 = PydanticOutputParser(pydantic_object=Feedback)

model = ChatGroq(
    model_name="llama3-70b-8192",
    api_key="GROQ_API_KEY",
    temperature=0.5)

parser = StrOutputParser()


prompt1 = PromptTemplate(
    template='Classify the sentiment of the following text into positive or negative {feedback} /n {format_instruction}',
    input_variables=['text'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)
prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feeedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feeedback}',
    input_variables=['feedback']
)
classifier_chain = prompt1 | model | parser2

branch_chain = RunnableBranch(
    (lambda x: x.sentiment=='positive' , prompt2|model|parser),
    (lambda x: x.sentiment=='negative' , prompt3|model|parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback':'this is a terrible phone'})
print(result)

