# Todo API

A simple RESTful API for managing todos built with FastAPI.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the API

To run the API locally:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the API is running, you can access:
- Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API documentation (ReDoc): `http://localhost:8000/redoc`

## API Endpoints

- `GET /todos`: Get all todos
- `GET /todos/{todo_id}`: Get a specific todo
- `POST /todos`: Create a new todo
- `PUT /todos/{todo_id}`: Update a todo
- `DELETE /todos/{todo_id}`: Delete a todo

## Running Tests

To run the tests:

```bash
pytest
```
