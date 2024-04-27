import random
from langchain.chains.llm import LLMChain
from langchain.chains.api.base import APIChain
# from langchain.chains.api import open_meteo_docs
# from api_gen import attack_question_by_llm, api_generation, defense
from glm import ChatZhipuAI
# from langchain.libs.langchain.langchain.chains.llm import LLMChain
# from langchain.libs.langchain.langchain.chains.api.base import APIChain
# from langchain.libs.langchain.langchain.chains.api import open_meteo_docs
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate

from json_attack import defense, generate_multi_attacked_api_response


# Define LLM:
zhipuai_api_key = "177a81bdda3ef0fee909d099d181ea1c.B8drennFRfzGfW0y"
llm = ChatZhipuAI(
    temperature=0.2,
    api_key=zhipuai_api_key,
    model="glm-4",
)

# main
question = "What is the weather like right now in Beijing, China in degrees Fahrenheit? What is the wind speed?"
# print answer
num_call = 4
mode = 0  # 0: print human-reable answer for each api response，1: Only return one human-reable answer for all the api responses
print(defense(question, generate_multi_attacked_api_response(
    llm,question, num_call), mode=mode))


