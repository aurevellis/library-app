from fastapi import APIRouter, HTTPException

from src.db import get_next_id, read_json, write_json
from src.models import Book, BookCreate

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=list[Book])
def list_books():
    return read_json("books.json")


@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    books = read_json("books.json")
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@router.post("/", response_model=Book, status_code=201)
def create_book(book: BookCreate):
    books = read_json("books.json")

    for existing in books:
        if existing["isbn"] == book.isbn:
            raise HTTPException(status_code=400, detail="Book with this ISBN already exists")

    new_book = {"id": get_next_id(books), **book.model_dump()}
    books.append(new_book)
    write_json("books.json", books)
    return new_book
