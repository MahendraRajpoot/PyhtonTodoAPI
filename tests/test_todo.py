import pytest
from src.models.todo import TodoCreate
from src.services.todo_service import TodoService

@pytest.fixture
def todo_service():
    return TodoService()

def test_create_todo(todo_service):
    todo_data = TodoCreate(
        title="Test Todo",
        description="This is a test todo",
        is_completed=False
    )
    todo = todo_service.create(todo_data)
    assert todo.title == "Test Todo"
    assert todo.description == "This is a test todo"
    assert todo.is_completed == False
    assert todo.id == 1

def test_get_todo(todo_service):
    todo_data = TodoCreate(
        title="Test Todo",
        description="This is a test todo",
        is_completed=False
    )
    created_todo = todo_service.create(todo_data)
    retrieved_todo = todo_service.get_by_id(created_todo.id)
    assert retrieved_todo is not None
    assert retrieved_todo.id == created_todo.id
    assert retrieved_todo.title == created_todo.title

def test_update_todo(todo_service):
    todo_data = TodoCreate(
        title="Test Todo",
        description="This is a test todo",
        is_completed=False
    )
    created_todo = todo_service.create(todo_data)
    
    updated_data = TodoCreate(
        title="Updated Todo",
        description="This is an updated todo",
        is_completed=True
    )
    updated_todo = todo_service.update(created_todo.id, updated_data)
    assert updated_todo is not None
    assert updated_todo.title == "Updated Todo"
    assert updated_todo.is_completed == True

def test_delete_todo(todo_service):
    todo_data = TodoCreate(
        title="Test Todo",
        description="This is a test todo",
        is_completed=False
    )
    created_todo = todo_service.create(todo_data)
    assert todo_service.delete(created_todo.id) == True
    assert todo_service.get_by_id(created_todo.id) is None
