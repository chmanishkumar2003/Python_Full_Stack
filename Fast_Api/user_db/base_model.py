from fastapi import FastAPI
from pydantic import BaseModel

#Base model for user
class User(BaseModel):
    name : str
    age  : int
    id   : int
    
app = FastAPI()

#Creating list to store users
user_db= []
@app.post("/users/")
def create(user : User):
    user_db.append(user)
    return {"message":"User added sucessfully","user":user}

@app.get("/users/")
def get_users():
    return {"count":len(user_db),"users":user_db}