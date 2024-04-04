Api interface encapsulation for chatglm2 (done but dropped)

Change the large language model as GLM4 (a model belong to chatglm series)

rewrite glm.py (mainly, the class ChatZhipuAI), in this case, GLM4 can be applied by langChain

*make GLM4 can be interact with api by using langChain through the class "langchain.chains.api.base.APIChain"

simulate Substitution-based Attack mechanism

make defense mechanism based on the Substitution-based Attack mechanism