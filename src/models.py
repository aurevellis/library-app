from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    author: str
    isbn: str
    copies: int = 1


class Book(BookCreate):
    id: int


class MemberCreate(BaseModel):
    name: str
    email: str


class Member(MemberCreate):
    id: int
    member_since: str


class BorrowRequest(BaseModel):
    book_id: int
    member_id: int


class Borrowing(BaseModel):
    id: int
    book_id: int
    member_id: int
    borrow_date: str
    due_date: str
    returned_date: str | None = None
