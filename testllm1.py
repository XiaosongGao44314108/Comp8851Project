from langchain.chains.api import open_meteo_docs
from langchain.chains.api.base import APIChain
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from glm import ChatZhipuAI
from api_gen import attack_question_by_llm, api_generation, defense

zhipuai_api_key = "a93655fab23b7874a0a98fff369245b4.4rnkIO3mGMCSj4oc"

llm = ChatZhipuAI(
    temperature=0.5,
    api_key=zhipuai_api_key,
    model="glm-4",
)

# messages = [
#     AIMessage(content="Hi."),
#     SystemMessage(content="Your role is a poet."),
#     HumanMessage(content="Write a short poem about AI in four lines."),
# ]
# response = llm.invoke(messages)
# print(response.content)

# from langchain_openai import OpenAI


chain = APIChain.from_llm_and_api_docs(
    llm=llm,
    api_docs=open_meteo_docs.OPEN_METEO_DOCS,
    verbose=True,
    limit_to_domains=["https://api.open-meteo.com/"],
)

# question = "What is the weather like right now in Munich, Germany in degrees Fahrenheit?"
# res = attack_question_by_llm(question)
# question_list = res.strip('\n')
# print(res)

# res = chain.run(
#     "What is the weather like right now in Munich, Germany in degrees Fahrenheit?"
# )
# print(res)
question = "What is the weather like right now in Munich, Germany in degrees Fahrenheit?"
print(defense(question, api_generation(chain, question, 2, 4)))
