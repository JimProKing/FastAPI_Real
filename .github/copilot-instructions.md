<!-- Guidance for AI coding agents working in this repository -->
# Copilot instructions — FastAPI_Real

Overview
- Small FastAPI example app. The app object lives in `todos/api.py` and mounts a router defined in `todos/todo.py`.
- Pydantic models are in `todos/model.py`. The router stores TODOs in an in-memory `todo_list` (no persistence).

Quick architecture
- Entry: `todos/api.py` — creates `FastAPI()` as `app` and does `app.include_router(todo_router)`.
- Router: `todos/todo.py` — defines `todo_router = APIRouter()` and endpoints: POST `/todo`, GET `/todo`, GET `/todo/{id}`.
- Models: `todos/model.py` — defines `Item` and `Todo` pydantic models (Todo references Item as a nested model).
- Dataflow: HTTP request -> pydantic validation (model) -> appended to `todo_list` -> returned JSON.

What to watch for (project-specific)
- `todos/todo.py` expects a `Todo` type for POST input; ensure you import it from `todos/model.py` (e.g. `from .model import Todo`) when editing that file.
- State is in-memory (`todo_list`); changes are ephemeral. For persistence work, introduce a DB layer and replace list usage.
- Router pattern: keep endpoint definitions inside `todo_router` and mount from `todos/api.py`.

Developer workflows / commands
- Run server locally (from project root):

```
uvicorn todos.api:app --reload --host 127.0.0.1 --port 8000
```

- Example requests (from README):

```
curl -X GET http://127.0.0.1:8000/todo -H "accept:application/json"

curl -X POST http://127.0.0.1:8000/todo \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "item": "First Todo is to finish this book!"}'
```

Common fixes an agent may apply
- Missing imports: add `from .model import Todo` to `todos/todo.py` and update type hints.
- Return shapes: endpoints return plain Pydantic models or dicts; prefer `return todo` or `return todo.dict()` if serializing.
- Path/Param metadata: use `fastapi.Path` or `Query` where helpful (existing usage of `Path(..., Title="...")` has a capitalized `Title` — use `title` instead).

Conventions and patterns
- Keep router definitions in `todos/todo.py` and avoid creating multiple app instances. `todos/api.py` is the single app root.
- Use Pydantic models for validation; nested models are used (see `Item` -> `Todo`).
- No tests currently — if adding tests, keep them alongside modules under a `tests/` folder and run via `pytest`.

Files to reference when editing or extending
- `todos/api.py` — app entry and router mounting.
- `todos/todo.py` — endpoint implementations and `todo_list` state.
- `todos/model.py` — pydantic model definitions.
- `README.md` — live curl examples and quick usage notes.

If something's unclear
- Ask for which file to edit and whether you should add persistence, tests, or type imports; mention a one-line proposed change before applying it.

End
