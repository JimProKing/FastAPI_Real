from pydantic import BaseModel

class Item(BaseModel):
    Item: str
    status: str

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