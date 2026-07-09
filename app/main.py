from fastapi import FastAPI
from app.database import engine, Base
from app.routes import items

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRUD API")

app.include_router(items.router)

@app.get("/")
def root():
    return {"message": "Welcome to the CRUD API"}
