import json
import requests

from langchain.llms.base import LLM
from langchain.llms.utils import enforce_stop_tokens
from typing import List, Optional

# API interface encapsulation

class ChatGLM2(LLM):
    max_token: int = 2048
    temperature: float = 0.1
    top_p = 0.7
    history = []
    # url="http://192.168.1.7:8000"
    # url="http://api.map.baidu.com/geocoding/v3/"
    url="http://192.168.1.7:8000"
    
    
    def __init__(self, temperature=temperature):
        super().__init__()
        self.temperature = temperature
        
    @property
    def _llm_type(self) -> str:
        return "ChatGLM2"
    
    def _call(self, prompt: str, stop: Optional[List[str]] = None,url=url) -> str:
        headers = {'Content-Type': 'application/json'}
        data = json.dumps({
            'prompt':prompt,
            'temperature':self.temperature, 
            'history':self.history,
            'max_length':self.max_token})
        print("ChatGLM prompt:", prompt)
        # api 
        response = requests.post(url, headers=headers, data=data, timeout=500)
        # response = requests.get(url, headers=headers, data=data, timeout=500)
        
        if response.status_code!=200:
            return "Researching result error"
        resp = response.json()
        if stop is not None:
            response = enforce_stop_tokens(response, stop)
        self.history = self.history + [[None, resp['response']]]
        return resp['response']