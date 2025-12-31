from fastapi import APIRouter
from model import Todo

todo_router = APIRouter()
todo_list = []

@todo_router.post("/todo")
#async def create_todo(todo: dict) -> dict: ## 유효성 검증을 위해, 입력값을 모델로 바꿀거임
async def create_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "Todo created successfully",
    }

@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {
        "todos": todo_list,
    }
