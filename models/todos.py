from pydantic import BaseModel

class Todo(BaseModel):
    name: str 
    password: str
    completed: bool

class Admin(BaseModel):
    username: str
    password: str


class Skin(BaseModel):
    filename: str
    contents: str
    rarity: str
    name: str
    value: int

    
    
