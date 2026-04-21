# Library App

A simple library book lending system API.

## Prerequisites

- Python 3.11+

## Setup

### Using uv (recommended)

```bash
pip install uv
uv sync
```

### Using pip

```bash
pip install fastapi uvicorn
```

## Running

### Using uv

```bash
uv run uvicorn src.main:app --reload
```

### Using pip

```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`.

API docs are available at `http://localhost:8000/docs`.

## API Endpoints

### Books
- `GET /books` — List all books
- `GET /books/{id}` — Get a book by ID
- `POST /books` — Add a new book

### Members
- `GET /members` — List all members
- `GET /members/{id}` — Get a member by ID
- `POST /members` — Register a new member

## Data

Data is stored as JSON files in the `data/` directory:
- `books.json` — Book catalogue
- `members.json` — Library members
