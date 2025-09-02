#Creating Url
from fastapi import FastAPI

app=FastAPI()

@app.get("/")

def root_url():
    return {'message':'Welcome to FastAPI'}

@app.get("/hub")
def root_url():
    return {'message':'Welcome to FastAPI,Internal Page'}
