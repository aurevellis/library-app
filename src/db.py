import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def read_json(filename: str) -> list[dict]:
    filepath = DATA_DIR / filename
    with open(filepath) as f:
        return json.load(f)


def write_json(filename: str, data: list[dict]) -> None:
    filepath = DATA_DIR / filename
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)


def get_next_id(records: list[dict]) -> int:
    if not records:
        return 1
    return max(r["id"] for r in records) + 1
