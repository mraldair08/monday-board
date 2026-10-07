import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class BoardService {

  private apiUrl = 'http://127.0.0.1:8001/api/boards';

  constructor(private http: HttpClient) {}

  getBoards() {
    return this.http.get(this.apiUrl);
  }
}