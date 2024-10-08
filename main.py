from fastapi import FastAPI

app = FastAPI()

app.title = "BOOKEASE"

@app.get("/")
def root() -> str:
    return "Hello World"