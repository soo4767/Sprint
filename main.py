from fastapi import FastAPI
from database import engine
from models import user, user_team, team_category, board_category, board, team, category, comment
from routers import user as user_route

app = FastAPI()

models = [
    user, user_team, team_category, board_category, board, team, category, comment
]
for model in models:
    model.Base.metadata.create_all(engine)

app.include_router(user_route.router)
