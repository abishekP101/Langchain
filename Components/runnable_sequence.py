from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence , RunnableParallel
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY1")

prompt  = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

model = ChatGroq(model_name="llama3-70b-8192",
                api_key=GROQ_API_KEY,
                temperature=0.7)

parser = StrOutputParser()

# prompt1 = PromptTemplate(
#     template="Explain the following joke:  {text}",
#     input_variables=['text']
# )

# chain = RunnableSequence(prompt , model , parser , prompt1 , model , parser)

# print(chain.invoke({'topic': 'AI'}))

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a linkedln post about {topic}',
    input_variables=['topic']
)

parallel_chain = RunnableParallel(
    {
        'tweet': RunnableSequence(prompt1 , model , parser),
        'linkedln': RunnableSequence(prompt2 , model , parser)
    }
)

result = parallel_chain.invoke({'topic':'AI'})
print(result)