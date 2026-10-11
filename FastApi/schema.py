from pydantic import BaseModel

class ResearchRequest(BaseModel):
    question:str
    thread_id:str|None =None

class Research_response(BaseModel):
    thread_id:str
    question:str
    answer:str
    sources: list[dict]
    verification:str



