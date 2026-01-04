# LV4
# 템플릿팅
- API 데이터를 화면에 표시
- 프론트엔드 컴포넌트처럼 처리
- Jinja 템플릿
  - 파이썬 모든 유형의 객체를 템플릿 변수로 사용 가능
  - 모델, 리스트, 딕셔너리
  - 문자열 수정 등을 Jinja에서 사용할 수 없음 -> 필터 사용 필요
필터 사용 예시
```py
{{ variable| filter_name(*args)}}
```
또는
```py
{{varibable | filter_name}}
```
1. ```{%%}```
- 구조 제어 명령
2. ```{{todo.item}}```
- 식의 값 전달
3. ```{#주석#}```
- 주석 기입 시 사용
- 웹페이지에는 표시안됨

# 자주 사용되는 필터
### 기본 필터
- 전달된 값이 None일 때
```py
{{todo.item|default('기본 아이템 입니다_todo')}}
```

### 이스케이프 필터
- HTML을 변환치않고 그대로 렌터링
```py
{{"<title>Todo App</title>"|escape}}
```

### 변환 필터
```py
{{3.1415|int}}
{{31|float}}
```

### 병합 필터
```py
{{['A','B','C']|join(' ')}}
# 결과: A B C
```

### 길이 필터
```py
Todo count: {{todos|length}}
```

### if문
```py
{% if todo | length < 5 %}
    할 일이 5개 미만입니다.
{% else %}
    바쁜 날을 보내고 있군요. 파이팅.
{% endif %}
```

### 반복문
```py
{% for todo in todos %}
    <b> {{todo.item}} </b>
{% endfor %}
```

### 매크로
- 하나의 함수로 HTML 문자열 반환
```py
{%macro input(name, value='', type='text', size=20 %)}
    <div class="form">
        <input type="{{type}}" name="{{name}}"
        value="{{value|escape}}" size="{{size}}">
    </div>
{% endmacro %}
# 호출방법(예시): {{input('item')}}
# 결과
<div class="form">
    <input type="text" name="item" value="" size="20">
```

### 템플릿 상속
- 중복 배제(DRY) 원칙에 근거
- 자식 템플릿 교체 가능

# Jinja2 사용하기
### 설치
```bash
pip install jinja2 python-multipart
mkdir templates
cd templates
touch {home,todo}.html
```
### POST 라우트 수정(todo.py)
```py
@todo_router.post("/todo", status_code=201)
#async def create_todo(todo: dict) -> dict: ## 유효성 검증을 위해, 입력값을 모델로 바꿀거임
async def create_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1  # 간단한 ID 할당
    todo_list.append(todo)
    return templates.TemplateResponse("todo_created.html", {"request": request, "todo": todo_list})
```

### GET 라우트 수정
```py
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(request: Request, todo_id: int = Path(..., Title="The ID of the todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse("todo.html", {"request": request, "todo": todo})
    # return {
    #     "message": "Todo not found",
    # }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
```

### model.py Config 서브클래스 추가
```py
from typing import Optional

class Todo(BaseModel):
    id: Optional[int]
    item: str

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)
```
