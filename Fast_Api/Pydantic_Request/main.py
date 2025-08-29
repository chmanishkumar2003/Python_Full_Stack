from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):
    name : str
    price : float
    offer: bool=None
    
@app.post("/items/")
def create(item:Item):
    return item 