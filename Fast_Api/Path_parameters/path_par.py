from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def root_url():
    return {'message':'Welcome to FastAPI'}

@app.get("/hub")
def root_url():
    return {'message':'Welcome to FastAPI,Internal Page'}

users ={
    "1":{"name":"Manish"},
    "2":{"name":"Harish Gandu"}
}

@app.get("/user/{user_id}")
def get_users(user_id):
    return users[user_id]