from fastapi import APIRouter
from models import Column, ColumnUpdate
from data import boards

router = APIRouter()

@router.post("/api/boards/{board_id}/columns")
def create_column(board_id: str, column: Column):
    for board in boards:
        if board.id == board_id:
            
            board.columns.append(column)
            
            for row in board.rows:
                row.cells[column.id] = ""
                
            return column
        
    return {"message": "Board no encontrado"}

@router.put("/api/boards/{board_id}/columns/{column_id}")
def update_column(board_id: str, column_id: str, update: ColumnUpdate):

    for board in boards:

        if board.id == board_id:

            for column in board.columns:

                if column.id == column_id:

                    column.name = update.name
                    column.type = update.type

                    return column

            return {"message": "Columna no encontrada"}

    return {"message": "Board no encontrado"}

@router.delete("/api/boards/{board_id}/columns/{column_id}")
def delete_column(board_id: str, column_id: str):

    for board in boards:

        if board.id == board_id:

            for column in board.columns:

                if column.id == column_id:

                    board.columns.remove(column)

                    for row in board.rows:
                        row.cells.pop(column_id, None)

                    return {"message": "Columna eliminada correctamente"}

            return {"message": "Columna no encontrada"}

    return {"message": "Board no encontrado"}