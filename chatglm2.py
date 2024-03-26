import json
import requests

from langchain.llms.base import LLM
from langchain.llms.utils import enforce_stop_tokens
from typing import List, Optional

class ChatGLM2(LLM):
    max_token: int = 2048
    temperature: float = 0.1
    top_p = 0.7
    history = []
    
    def __init__(self, temperature=temperature):
        super().__init__()
        self.temperature = temperature
        
    @property
    def _llm_type(self) -> str:
        return "ChatGLM2"
    
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {'Content-Type': 'application/json'}
        data = json.dumps({
            'prompt':prompt,
            'temperature':self.temperature, 
            'history':self.history,
            'max_length':self.max_token})
        print("ChatGLM prompt:", prompt)
        # 调用api 
        response = requests.post("http://192.168.1.7:8000", headers=headers, data=data, timeout=500)
        if response.status_code!=200:
            return "查询结果错误"
        resp = response.json()
        if stop is not None:
            response = enforce_stop_tokens(response, stop)
        self.history = self.history + [[None, resp['response']]]
        return resp['response']