from pydantic import BaseModel
from typing import List

class CodeSnippet(BaseModel):
    code: str
    
class ResponseItem(BaseModel):
    explaination: str
    time_complexity: str
    optimized_code: str
    
class CodeResponse(BaseModel):
    results: List[ResponseItem]