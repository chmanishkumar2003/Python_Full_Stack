from fastapi import FastAPI, HTTPException

app = FastAPI()

users = {
    1: {"name": "Manish"},
    2: {"name": "Harish Gandu"},
    3: {"name": "Hashit"},
    4: {"name": "Harsha"}
}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User id not found / not in user list")
    return users[user_id]

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id in users:
        del users[user_id]
        return {"Deleted": user_id}
    raise HTTPException(status_code=404, detail="User id not found / not in users list")

@app.get("/mydocs")
def get_docs():
    return {"docs_url": "http://127.0.0.1:8000/docs"}
