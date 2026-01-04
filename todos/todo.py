# 얘가 라우터 역할 하고있음
from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, HTMLResponse  # 추가
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()
todo_list = []
templates = Jinja2Templates(directory="templates/")

# @todo_router.post("/todo", status_code=201)
# #async def create_todo(todo: dict) -> dict: ## 유효성 검증을 위해, 입력값을 모델로 바꿀거임
# async def create_todo(todo: Todo) -> dict:
#     todo_list.append(todo)
#     return {
#         "message": "Todo created successfully",
#     }

# 최종 버전: 추가 후 목록 페이지로 리다이렉트 (PRG 패턴)
@todo_router.post("/todo")
async def create_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1  # 간단한 ID 할당
    todo_list.append(todo)
    # 템플릿 직접 렌더링 대신 리다이렉트 → GET /todo 호출됨
    return RedirectResponse(url="/todo", status_code=303)


# 전체 목록 페이지 (브라우저에서 /todo 접속 시)
@todo_router.get("/todo", response_class=HTMLResponse)
async def retrieve_todos(request: Request):
    return templates.TemplateResponse(
        "todo.html",
        {"request": request, "todos": todo_list}
    )


# @todo_router.get("/todo/{todo_id}")
# async def get_single_todo(todo_id: int = Path(..., Title="The ID of the todo to retrieve")) -> dict:
#     for todo in todo_list:
#         if todo.id == todo_id:
#             return {
#                 "todo": todo,
#             }
#     # return {
#     #     "message": "Todo not found",
#     # }
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

# 개별 Todo 상세 페이지 (/todo/{todo_id})
@todo_router.get("/todo/{todo_id}", response_class=HTMLResponse)
async def get_single_todo(
    request: Request,
    todo_id: int = Path(..., title="The ID of the todo to retrieve")
):
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse(
                "todo.html",
                {"request": request, "todos": todo_list, "todo": todo}  # 전체 목록 + 현재 todo 전달
            )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")


@todo_router.put("/todo/{todo_id}")
async def update_todo(
    todo_data: TodoItem,
    todo_id: int = Path(..., title="The ID of the todo to update")
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"message": "Todo updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")


@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")


@todo_router.delete("/todo")
async def delete_all_todos() -> dict:
    todo_list.clear()
    return {"message": "All todos deleted successfully"}