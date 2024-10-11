from fastapi import FastAPI
from src.router.seed import seed
from src.router.search import search

app = FastAPI()
app.title = "BOOKEASE"
app.include_router(seed.router, tags=["seed"])
app.include_router(search.router, tags=["search"])

@app.get("/")
def root() -> str:
    return "Hello World"