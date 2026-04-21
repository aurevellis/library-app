from fastapi import FastAPI

from src.routes import books, borrowings, members

app = FastAPI(title="Library App", version="1.0.0")

app.include_router(books.router)
app.include_router(members.router)
app.include_router(borrowings.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
