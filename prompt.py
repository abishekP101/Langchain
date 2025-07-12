from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""Summarize research paper {paper_input} with the  length {length_input}
    and style should be {style_input} """,
input_variables = ['paper_input' , 'length_input', 'style_input']
)

template.save('template.json')