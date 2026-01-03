# LV3
260103
### pydantic 사용
서버에 전달된 요청을 기준으로 적절한 응답을 렌더링
> 오류처리
>> 상태코드 + 오류 메시지

### 상태코드 
- 1: 받음
- 2: 성공적 처리
- 3: 리다이렉트
- 4: 클라 오류
- 5: 서버 오류 

### Mission: todo 배열에 저장된 모든 값이 아닌, todo 아이템만 반환하도록 (id 없이)

### response 지정하기
```py
@todo_router.get("/todo", response_model=TodoItems)
```
이런식으로 response_model을 지정해줄 수 있음

```py
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
 ```

 # 오류처리
 가령, 존재하지 않는 id로 get_single_todo 요청하면 200으로 반환됨.
 ```json
{
  "message": "Todo not found"
}
 ```
- 이런 경우, 404에러를 반환하도록
### 라우터에 raise 구문 추가
```py
    # return {
    #     "message": "Todo not found",
    # }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found") 

```
# 성공응답 상태코드 변경
add_todo (post) 성공 시 200코드 출력되는데, 201로 변경
- 데코레이터에 status_code 파라미터 추가
```py
@todo_router.post("/todo", status_code=201)
#async def create_todo(todo: dict) -> dict: ## 유효성 검증을 위해, 입력값을 모델로 바꿀거임
async def create_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "Todo created successfully",
    }
```

