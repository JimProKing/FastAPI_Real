# 얘가 라우터 역할 하고있음
from fastapi import APIRouter, Path, HTTPException, status
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()
todo_list = []

@todo_router.post("/todo", status_code=201)
#async def create_todo(todo: dict) -> dict: ## 유효성 검증을 위해, 입력값을 모델로 바꿀거임
async def create_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "Todo created successfully",
    }

@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todos() -> dict:
    return {
        "todos": todo_list,
    }
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., Title="The ID of the todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo,
            }
    # return {
    #     "message": "Todo not found",
    # }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., Title="The ID of the todo to update")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Todo updated successfully",
            }
    # return {
    #     "message": "Todo not found",
    # }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found") 

@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int)-> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted successfully",
            }
    # return {
    #     "message": "Todo not found",
    # }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found") 

@todo_router.delete("/todo")
async def delete_all_todos() -> dict:
    todo_list.clear()
    return {
        "message": "All todos deleted successfully",
    }

