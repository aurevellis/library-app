import os
from datetime import date, timedelta

from fastapi import APIRouter, HTTPException

from src.db import get_next_id, read_json, write_json
from src.models import BorrowRequest, Borrowing

router = APIRouter(prefix="/borrowings", tags=["borrowings"])


@router.get("/")
def list_borrowings():
    return read_json("borrowings.json")


@router.get("/{borrowing_id}")
def get_borrowing(borrowing_id: int):
    borrowings = read_json("borrowings.json")

    for borrowing in borrowings:
        if borrowing["id"] == borrowing_id:
            return borrowing

    return {"message": "Borrowing not found"}


@router.put("/")
def borrow_book(request: BorrowRequest):
    borrowings = read_json("borrowings.json")

    today = date.today()
    new_borrowing = {
        "id": get_next_id(borrowings),
        "book_id": request.book_id,
        "member_id": request.member_id,
        "borrow_date": today.isoformat(),
        "due_date": (today + timedelta(days=14)).isoformat(),
        "returned_date": None,
    }
    borrowings.append(new_borrowing)
    write_json("borrowings.json", borrowings)
    return new_borrowing


@router.delete("/{borrowing_id}")
def delete_borrowing(borrowing_id: int):
    borrowings = read_json("borrowings.json")

    borrowings = [b for b in borrowings if b["id"] != borrowing_id]

    return {"message": "Borrowing deleted"}
