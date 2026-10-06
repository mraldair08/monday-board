import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BoardService } from './services/board';

@Component({
  selector: 'app-root',
  imports: [CommonModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App implements OnInit {

  boards: any = null;

  editingCell: {
    rowId: string;
    columnId: string;
  } | null = null;

  constructor(private boardService: BoardService) {}

  ngOnInit() {

    this.boardService.getBoards().subscribe({
      next: (data) => {

        console.log('Respuesta completa:', data);
        console.log('Tipo:', typeof data);
        console.log('Boards dentro de data:', data.boards);

        this.boards = data.boards;

      },

      error: (error) => {

        console.error(
          'Error al obtener los boards:',
          error
        );

      }
    });

  }

  addRow() {

    const board = this.boards[0];

    const newRow = {
      cells: {
        task: 'Nueva tarea',
        status: 'Pendiente',
        date: '2026-10-07'
      }
    };

    this.boardService.createRow(
      board.id,
      newRow
    ).subscribe({

      next: (data) => {

        console.log(
          'Nueva fila creada:',
          data
        );

        this.boards[0].rows.push(data);

      },

      error: (error) => {

        console.error(
          'Error al crear la fila:',
          error
        );

      }

    });

  }

  editCell(row: any, column: any) {

    this.editingCell = {
      rowId: row.id,
      columnId: column.id
    };

  }

  saveCell(
    row: any,
    column: any,
    value: string
  ) {

    this.boardService.updateRow(
      this.boards[0].id,
      row.id,
      {
        [column.id]: value
      }
    ).subscribe({

      next: (data) => {

        console.log(
          'Celda actualizada:',
          data
        );

        row.cells[column.id] = value;

        this.editingCell = null;

      },

      error: (error) => {

        console.error(
          'Error al actualizar la celda:',
          error
        );

      }

    });

  }

}
