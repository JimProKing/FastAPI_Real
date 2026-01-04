from pydantic import BaseModel
from fastapi import Form
from typing import List, Optional

# 불필요하거나 사용 안 하면 삭제 가능
# class Item(BaseModel):
#     item: str
#     status: str

# 새 Todo 생성 시 사용할 모델 (폼에서 item만 받음)
class TodoItem(BaseModel):
    item: str

    model_config = {
        "json_schema_extra": {
            "examples": [{"item": "새로운 할 일"}]
        }
    }

# 실제 저장하고 반환할 Todo 모델 (id 포함)
class Todo(BaseModel):
    id: Optional[int] = None
    item: str

    model_config = {
        "json_schema_extra": {
            "examples": [{"id": 1, "item": "예시 할 일"}]
        }
    }

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)  # id는 서버에서 생성

# 여러 Todo 반환용
class TodoItems(BaseModel):
    todos: List[Todo]  # id 포함된 Todo 리스트

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "todos": [
                        {"id": 1, "item": "Example schema 1!"},
                        {"id": 2, "item": "Example schema 2!"}
                    ]
                }
            ]
        }
    }