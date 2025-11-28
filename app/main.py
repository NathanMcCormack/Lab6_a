from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

app = FastAPI(title="Service A - Greeting API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name} from Service A!"}