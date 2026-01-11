#For rasing exception in fast api we need to import HTTP Exeception

from fastapi import FastAPI,HTTPException

app=FastAPI()

@app.get("/")

def root_url():
    return {'message':'Welcome to FastAPI'}

@app.get("/hub")
def root_url():
    return {'message':'Welcome to FastAPI,Internal Page'}

users ={
    1:{"name":"Manish"},
    2:{"name":"Harish Gandu"}
}

@app.get("/user/{user_id}")
def get_users(user_id:int):
    if user_id not in users:
        raise HTTPException(status_code=404,detail="User id not found/not in user list")
    return users[user_id]