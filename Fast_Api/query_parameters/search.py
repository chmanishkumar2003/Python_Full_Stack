from fastapi import FastAPI
from typing import Optional

app=FastAPI()

items=[
    {"id":1,"name":"Pen","cate":"Stationary","price":20},
    {"id":2,"name":"Pencil","cate":"Stationary","price":10},
    {"id":3,"name":"Eraser","cate":"Stationary","price":10},
    {"id":4,"name":"Stapler","cate":"Stationary","price":50},
    {"id":5,"name":"Gombox","cate":"Stationary","price":150},
    {"id":6,"name":"G-Vagon","cate":"Car","price":5555555},

]

@app.get("/products")
def search(cate:Optional[str]=None,max:Optional[int]=None):
    filter=items
    if cate:
        filter=[i for i in filter if i['cate'].lower()==cate.lower()]
    
    if max:
        filter=[i for i in filter if i['price'] <= max]
    
    return filter