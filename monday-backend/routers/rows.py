from fastapi import APIRouter
from models import Row, RowUpdate
from data import boards

router = APIRouter()

@router.post("/api/boards/{board_id}/rows")
def create_row(board_id: str, row: Row):
    for board in boards:
        if board.id == board_id:
            board.rows.append(row)
            return row
        
    return{"message": "Board no encontrado"}

@router.put("/api/boards/{board_id}/rows/{row_id}")
def update_row(board_id: str, row_id: str, update: RowUpdate):

    for board in boards:
        if board.id == board_id:

            for row in board.rows:
                if row.id == row_id:

                    row.cells.update(update.cells)

                    return row

            return {"message": "Fila no encontrada"}

    return {"message": "Board no encontrado"}

@router.delete("/api/boards/{board_id}/rows/{row_id}")
def delete_row(board_id: str, row_id: str):

    for board in boards:
        if board.id == board_id:

            for row in board.rows:
                if row.id == row_id:

                    board.rows.remove(row)

                    return {"message": "Fila eliminada correctamente"}

            return {"message": "Fila no encontrada"}

    return {"message": "Board no encontrado"}