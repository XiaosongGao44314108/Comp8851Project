from langchain import PromptTemplate
from chatglm2 import ChatGLM2
import json




llm = ChatGLM2(temperature=0.1)

text = 'hello'

def answerThis(Question):
    text=Question
    template = """
    Only return the most important information based on the following content:
    
    {text}
    """
    prompt = PromptTemplate(
   input_variables=["text"],
   template=template,
    )
    prompt_format = prompt.format(text=text)
    output = llm(prompt_format)
    print(output)

answerThis(text)
