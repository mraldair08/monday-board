from fastapi import FastAPI
from uuid import uuid4
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Monday Style Board")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Column(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    type: str

class Row(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    cells: dict[str, str]

class RowUpdate(BaseModel):
    cells: dict[str, str]
    
class ColumnUpdate(BaseModel):
    name: str
    type: str

class Board(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    title: str
    columns: list[Column]
    rows: list[Row]


boards = [
    Board(
        title="Mi primer tablero",
        columns=[
            Column(id="task", name="Tarea", type="text"),
            Column(id="status", name="Estado", type="status"),
            Column(id="date", name="Fecha", type="date")
        ],
        rows=[
            Row(
                cells={
                    "task": "Aprender Angular",
                    "status": "En progreso",
                    "date": "2026-10-06"
                }
            ),
            Row(
                cells={
                    "task": "Conectar FastAPI",
                    "status": "Completado",
                    "date": "2026-10-05"
                }
            )
        ]
    )
]


@app.get("/")
def home():
    return {"message": "Monday Style Board API funcionando"}


@app.get("/api/boards")
def get_boards():
    return {"boards": boards}


@app.post("/api/boards")
def create_board(board: Board):
    boards.append(board)
    return board


@app.post("/api/boards/{board_id}/rows")
def create_row(board_id: str, row: Row):
    for board in boards:
        if board.id == board_id:
            board.rows.append(row)
            return row
        
    return{"message": "Board no encontrado"}

@app.put("/api/boards/{board_id}/rows/{row_id}")
def update_row(board_id: str, row_id: str, update: RowUpdate):

    for board in boards:
        if board.id == board_id:

            for row in board.rows:
                if row.id == row_id:

                    row.cells.update(update.cells)

                    return row

            return {"message": "Fila no encontrada"}

    return {"message": "Board no encontrado"}

@app.delete("/api/boards/{board_id}/rows/{row_id}")
def delete_row(board_id: str, row_id: str):

    for board in boards:
        if board.id == board_id:

            for row in board.rows:
                if row.id == row_id:

                    board.rows.remove(row)

                    return {"message": "Fila eliminada correctamente"}

            return {"message": "Fila no encontrada"}

    return {"message": "Board no encontrado"}

@app.post("/api/boards/{board_id}/columns")
def create_column(board_id: str, column: Column):
    for board in boards:
        if board.id == board_id:
            
            board.columns.append(column)
            
            for row in board.rows:
                row.cells[column.id] = ""
                
            return column
        
    return {"message": "Board no encontrado"}

@app.put("/api/boards/{board_id}/columns/{column_id}")
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

@app.delete("/api/boards/{board_id}/columns/{column_id}")
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