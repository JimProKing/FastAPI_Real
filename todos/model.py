from pydantic import BaseModel

# # 기본형
# class Todo(BaseModel):
#     id: int
#     item: str

# 중첩 모델
class Item(BaseModel):
    Item: str
    status: str

class Todo(BaseModel):
    id: int
    item: Item