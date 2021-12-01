from fastapi import FastAPI
from database import engine
from models import user

app = FastAPI()

user.Base.metadata.create_all(engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}
