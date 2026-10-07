from fastapi import APIRouter
from models import Row, RowUpdate
from services.row_service import (
    create_row,
    update_row,
    delete_row
    )

router = APIRouter()

@router.post("/api/boards/{board_id}/rows")
def create_row(board_id: str, row: Row):
    return create_row(board_id, row)

@router.put("/api/boards/{board_id}/rows/{row_id}")
def update_row(board_id: str, row_id: str, update: RowUpdate):
    return update_row(board_id, row_id, update)

@router.delete("/api/boards/{board_id}/rows/{row_id}")
def delete_row(board_id: str, row_id: str):
    return delete_row(board_id, row_id)