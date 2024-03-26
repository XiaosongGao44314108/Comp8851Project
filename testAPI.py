from langchain import PromptTemplate
from chatglm2 import ChatGLM2

llm = ChatGLM2(temperature=0.1)

template = """
    根据以下内容，提取最重要信息。
    
    {text}
"""
prompt = PromptTemplate(
   input_variables=["text"],
   template=template,
)
text = '世界最高峰是？'
prompt_format = prompt.format(text=text)
output = llm(prompt_format)
print(output)