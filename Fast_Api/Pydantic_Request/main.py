from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    offer: bool = None

# POST → Create new resource
@app.post("/item/")
def create(item: Item):
    return {"message": "Item created successfully", "item": item}

# GET → Retrieve data (with optional query parameter)
@app.get("/items/")
def get(name: str = None):
    if name:
        return {"message": f"Fetching item with name {name}"}
    return {"message": "Fetching all items"}
