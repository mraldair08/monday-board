from fastapi import APIRouter
from models import Column, ColumnUpdate
from data import boards
from services.column_service import (
    create_column,
    update_column,
    delete_column
)

router = APIRouter()

@router.post("/api/boards/{board_id}/columns")
def create_column(board_id: str, column: Column):
    return create_column(board_id, column)

@router.put("/api/boards/{board_id}/columns/{column_id}")
def update_column(board_id: str, column_id: str, update: ColumnUpdate):
    return update_column(board_id, column_id, update)

@router.delete("/api/boards/{board_id}/columns/{column_id}")
def delete_column(board_id: str, column_id: str):
    return delete_column(board_id, column_id)