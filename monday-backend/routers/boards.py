
from fastapi import APIRouter
from models import Board
from data import boards


router = APIRouter()

@router.get("/api/boards")
def get_board():
    return {"boards": boards}

@router.post("/api/boards")
def create_board(board: Board):
    boards.append(board)
    return board