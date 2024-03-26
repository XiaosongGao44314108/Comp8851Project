from langchain import PromptTemplate
from chatglm2 import ChatGLM2

llm = ChatGLM2(temperature=0.1)

template = """
    内容生成任务：请根据下面的提示，生成一段文本。
    
    {text}
"""
prompt = PromptTemplate(
   input_variables=["text"],
   template=template,
)
text = '今天是个好天气，'
prompt_format = prompt.format(text=text)
output = llm(prompt_format)
print(output)