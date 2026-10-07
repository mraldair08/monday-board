from fastapi import FastAPI, APIRouter
from uuid import uuid4
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from routers import boards, rows, columns

app = FastAPI(title="Monday Style Board")
router = APIRouter()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(boards.router)
app.include_router(rows.router)
app.include_router(columns.router)


@app.get("/")
def home():
    return {"message": "Monday Style Board API funcionando"}





