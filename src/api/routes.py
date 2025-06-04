from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ..models.todo import Todo, TodoCreate
from ..services.todo_service import TodoService

router = APIRouter(prefix="/todos", tags=["todos"])
todo_service = TodoService()

@router.get("/", response_model=List[Todo])
async def get_todos():
    return todo_service.get_all()

@router.get("/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    todo = todo_service.get_by_id(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/", response_model=Todo)
async def create_todo(todo: TodoCreate):
    return todo_service.create(todo)

@router.put("/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo: TodoCreate):
    updated_todo = todo_service.update(todo_id, todo)
    if updated_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo

@router.delete("/{todo_id}")
async def delete_todo(todo_id: int):
    if not todo_service.delete(todo_id):
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
