# LV2 
251231

# 라우터
> 서버로 전송된 요청을 처리하는 함수
> 
> ex) 서버로 전송된 요청을 처리

### 기본 과정
> 1. todo.py 작성
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
