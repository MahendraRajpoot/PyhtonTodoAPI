from datetime import datetime
from typing import List, Optional
from ..models.todo import Todo, TodoCreate

class TodoService:
    def __init__(self):
        self.todos = []
        self.counter = 0

    def get_all(self) -> List[Todo]:
        print("Hello This is a test")
        return self.todos

    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        return next((todo for todo in self.todos if todo.id == todo_id), None)

    def create(self, todo_create: TodoCreate) -> Todo:
        self.counter += 1
        now = datetime.now()
        todo = Todo(
            id=self.counter,
            title=todo_create.title,
            description=todo_create.description,
            is_completed=todo_create.is_completed,
            created_at=now,
            updated_at=now
        )
        self.todos.append(todo)
        return todo

    def update(self, todo_id: int, todo_update: TodoCreate) -> Optional[Todo]:
        todo = self.get_by_id(todo_id)
        if todo is None:
            return None
        
        todo.title = todo_update.title
        todo.description = todo_update.description
        todo.is_completed = todo_update.is_completed
        todo.updated_at = datetime.now()
        return todo

    def delete(self, todo_id: int) -> bool:
        todo = self.get_by_id(todo_id)
        if todo is None:
            return False
        self.todos.remove(todo)
        return True
