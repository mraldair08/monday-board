from models import Board, Column, Row

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