
from fastapi import APIRouter
from models import Board
from data import boards
from services.board_service import (
    create_boards
)


router = APIRouter()

@router.get("/api/boards")
def get_board():
    return {"boards": boards}

@router.post("/api/boards")
def create_board_route(board: Board):
    return board