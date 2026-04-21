from datetime import date, timedelta

from fastapi import APIRouter, HTTPException

from src.db import get_next_id, read_json, write_json
from src.models import BorrowRequest, Borrowing

router = APIRouter(prefix="/borrowings", tags=["borrowings"])

LOAN_PERIOD_DAYS = 14


@router.get("/", response_model=list[Borrowing])
def list_borrowings():
    return read_json("borrowings.json")


@router.post("/", response_model=Borrowing, status_code=201)
def borrow_book(request: BorrowRequest):
    books = read_json("books.json")
    members = read_json("members.json")
    borrowings = read_json("borrowings.json")

    book = next((b for b in books if b["id"] == request.book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    member = next((m for m in members if m["id"] == request.member_id), None)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")

    active_borrows = [
        br for br in borrowings
        if br["book_id"] == request.book_id and br["returned_date"] is None
    ]
    if len(active_borrows) >= book["copies"]:
        raise HTTPException(status_code=400, detail="No copies available for borrowing")

    today = date.today()
    new_borrowing = {
        "id": get_next_id(borrowings),
        "book_id": request.book_id,
        "member_id": request.member_id,
        "borrow_date": today.isoformat(),
        "due_date": (today + timedelta(days=LOAN_PERIOD_DAYS)).isoformat(),
        "returned_date": None,
    }
    borrowings.append(new_borrowing)
    write_json("borrowings.json", borrowings)
    return new_borrowing
