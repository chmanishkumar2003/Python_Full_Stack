#Query parameters are use cases are for filter,search and sorting .
#Query parameter is a value after ? mark in the url used to customization without affecting end point path.



from fastapi import FastAPI

app=FastAPI()
@app.get("/search/")
def search(q:str=None,limit: int=10):
    return{"query":q,"limit":limit}

@app.get("/docs")

def docs():
    return{"docs_url":"http://127.0.0.1:8000/docs"}