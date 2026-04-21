from datetime import date

from fastapi import APIRouter, HTTPException

from src.db import get_next_id, read_json, write_json
from src.models import Member, MemberCreate

router = APIRouter(prefix="/members", tags=["members"])


@router.get("/", response_model=list[Member])
def list_members():
    return read_json("members.json")


@router.get("/{member_id}", response_model=Member)
def get_member(member_id: int):
    members = read_json("members.json")
    for member in members:
        if member["id"] == member_id:
            return member
    raise HTTPException(status_code=404, detail="Member not found")


@router.post("/", response_model=Member, status_code=201)
def create_member(member: MemberCreate):
    members = read_json("members.json")

    for existing in members:
        if existing["email"] == member.email:
            raise HTTPException(status_code=400, detail="Member with this email already exists")

    new_member = {
        "id": get_next_id(members),
        **member.model_dump(),
        "member_since": date.today().isoformat(),
    }
    members.append(new_member)
    write_json("members.json", members)
    return new_member
