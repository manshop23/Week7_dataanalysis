from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class User(BaseModel):
    username:str
    password:str
    level: Optional[str] = "nomal"

@app.get("/")
def read_root():
    return {"Hello": "World"}

#http://127.0.0.1:8000/hi?name=manny&reply=1234
@app.get("/hi")
def hi(name:str, reply:str  ): 
    return {"hi": name,"reply": reply}

#http://127.0.0.1:8000/items/1
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/login")
def login(user : User):
    return {"echo": user}
@app.post("/login")
def login(user : User):
    return {"echo": user}
