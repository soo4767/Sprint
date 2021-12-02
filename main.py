from fastapi import FastAPI
from database import engine
from models import user, user_team, team_category, board_category, board, team, category, comment
from routers import user as user_route
from routers import team as team_route
from routers import board as board_route
from routers import comment as comment_route
from routers import category as category_route

app = FastAPI()

models = [
    user, user_team, team_category, board_category, board, team, category, comment
]
for model in models:
    model.Base.metadata.create_all(engine)

app.include_router(user_route.router)
app.include_router(team_route.router)
app.include_router(board_route.router)
# app.include_router(comment_route.router)
app.include_router(category_route.router)

import uvicorn
from pathlib import Path
import os
import sys

if __name__ == "__main__":
    path = Path(os.path.realpath(__file__)).parent.parent.absolute()
    sys.path.append(str(path))
    uvicorn.run("spint.main:app", host="0.0.0.0", reload=True, port=8000)
