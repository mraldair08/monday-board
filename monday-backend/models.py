from pydantic import BaseModel, Field
from uuid import uuid4

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
