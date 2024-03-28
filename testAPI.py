from langchain import PromptTemplate
from chatglm2 import ChatGLM2

llm = ChatGLM2(temperature=0.1)

template = """
    Only return the most important information based on the following content.
    
    {text}
"""
prompt = PromptTemplate(
   input_variables=["text"],
   template=template,
)
text = 'What is the highest mountain in the world?'
prompt_format = prompt.format(text=text)
output = llm(prompt_format)
print(output)