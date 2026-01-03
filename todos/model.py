# 요청 주고받을 형식을 지정
from pydantic import BaseModel

from typing import List

class Item(BaseModel):
    Item: str
    status: str

# id, item 둘 다 있음
class Todo(BaseModel):
    id: int
    item: str

    model_config = {
        "json_schema_extra": {
            "examples": [  # 여러 개 가능, 단일 예시도 리스트로
                {
                    "id": 1,
                    "item": "예시 할 일"
                }
            ]
        }
    }

# item만 있음
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

# 여러 개의 TodoItem을 담는 모델
class TodoItems(BaseModel):
    todos: List[TodoItem]

    # Pydantic v2 방식: model_config 사용
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "todos": [
                        {"item": "Example schema 1!"},
                        {"item": "Example schema 2!"}
                    ]
                }
            ]
        }
    }