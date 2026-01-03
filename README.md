# LV2 
251231

> **!! uvicorn 서버 시작법**
> 
> ```unicornn api:app --port 8000 --reload```

# 라우터
> 서버로 전송된 요청을 처리하는 함수
> 
> ex) 서버로 전송된 요청을 처리

### 기본 과정
> 1. todo.py 작성 (여기서 라우터 만들거임)
> 2. api.py에 import 추가
> ```from todo import todo_router```

### GET 요청
```curl -X GET http://127.0.0.1:8000/todo -H "accept:application/json"```
### POST 요청
```
curl -X POST http://127.0.0.1:8000/todo \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "item": "First Todo is to finish this book!"}'
```
### pydantic 모델
- 정의된 데이터만 전송되도록 바디를 검증
``` from pydantic import BaseModel ```
- model.py 만들고, 코드 추가해서 유효성 검증 가능하도록 함.
  - todo.py(라우터)에서 import 해서 쓰면 됨

### pydantic 클래스 정의
```model.py
from pydantic Import BaseModel

class Todo(BaseModel):
    id: int
    item: str
```

### pydantic 중첩 모델
```model.py
class Item(BaseModel):
    Item: str
    status: str

class Todo(BaseModel):
    id: int
    item: Item
```
* 중첩해서 사용 가능하다는 건 확인했지만, ```item: str```으로 계속 쓰자

### 경로 매개변수
```todo_router.post("/todo/{todo_id}")```

### Path 파라미터
![alt text](image.png)
이렇게 swagger 문서에 필수값, 설명 등등을 

# get_single_todo
```python
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return{
                "todo":todo
            }
    return {
        "message":"Todo not found"
    }
```
### GET 요청으로 테스트
```bash
curl -X 'GET' \
'http://127.0.0.1:8000/todo/1' \
-H 'accept: application/json'
```
### ReDoc 문서
 http://127.0.0.1:8000/redoc
 접속

 # update_todo
 ### 요청 바디 모델 (model.py)
 ```python
class TodoItem(BaseModel):
    item: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "item": "예시 할 일"
                }
            ]   
        }
    }
    ### 주의) pydantic 버전에 따라 형식이 다름
 ```

### 라우트 추가 (todo.py)
```python
from model import TodoItem
# update를 위한 모델을 추가했으니, import

todo_router = APIRouter()

@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., Title="The ID of the todo to update")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Todo updated successfully",
            }
    return {
        "message": "Todo not found",
    }
```

# delete_single_todo
### 라우트 추가
```python
todo_router = APIRouter()

@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int)-> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted successfully",
            }
    return {
        "message": "Todo not found",
    }

@todo_router.delete("/todo")
async def delete_all_todos() -> dict:
    todo_list.clear()
    return {
        "message": "All todos deleted successfully",
    }
```