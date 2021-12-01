from fastapi import FastAPI
from database import engine
from models import user, user_team, team_category, board_layer, board_category, board, team, category, comment

app = FastAPI()

models = [
    user, user_team, team_category, board_layer, board_category, board, team, category, comment
]
for model in models:
    model.Base.metadata.create_all(engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}
