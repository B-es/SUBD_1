from pydantic import BaseModel

class Chat(BaseModel):
    userId1:str
    userId2:str
    messages:list[str]