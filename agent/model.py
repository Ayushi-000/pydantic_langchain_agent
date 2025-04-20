from pydantic import BaseModel

class Query(BaseModel):
    task_type: str
    prompt: str

class Response(BaseModel):
    result: str
