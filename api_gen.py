from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
# from langchain_community.llms import OpenAI
import os
import random
from glm import ChatZhipuAI

# from testllm1 import
zhipuai_api_key = "a93655fab23b7874a0a98fff369245b4.4rnkIO3mGMCSj4oc"

llm = ChatZhipuAI(
    temperature=0.9,
    api_key=zhipuai_api_key,
    model="glm-4",
)


def attack_question_by_llm(question):

    prompt = PromptTemplate(
        input_variables=["question"],
        template="""
        Write an identical sentence modelled on {question}. You can change the country, city, time, etc.
        requiring the rewritten sentence to have exactly the same syntax as the original input.
        Attention! You only need to return two rewritten sentences 
        Don't return extra words!
        """
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(question)


def api_generation(chain, question, rate, total_num):
    res = attack_question_by_llm(question)
    question_list = res.split('\n')

    answer_list = []
    for i in range(total_num):
        random_number = random.randint(0, rate)

        if random_number == 0:
            question = random.choice(question_list)

        answer_list.append(f'{i}:' + chain.run(question))

    # print(answer_list)

    return str(answer_list)


def defense(question, answer):
    prompt = PromptTemplate(
        input_variables=["answer"],
        template="""
        There are now multiple responses {answer} to the original question, so please return the correct answer based on the 
        original question. And when there are inconsistencies in multiple answers, add the exactly following content to the 
        output: 'Malicious behaviour detected, this answer may have been tampered with.'
        If there is no correct answer, please directly output: Wrong answer detected.
        """
    )
    prompt.template += f"This is the original question: {question}"

    chain = LLMChain(llm=llm, prompt=prompt)
    res = chain.run(answer)
    return res


if __name__ == "__main__":
    question = "What is the weather like right now in Munich, Germany in degrees Fahrenheit?"
    # res = attack_question_by_llm(question)
    # question_list = res.strip('\n')
    # print(res)
    # api_generation(1, question, 1, 10)
    # print(defense(question, api_generation(1, question, 1, 10)))
