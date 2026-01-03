from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Message": "Hello World"}

##### 라우터 추가 #####
from todo import todo_router

app.include_router(todo_router)11