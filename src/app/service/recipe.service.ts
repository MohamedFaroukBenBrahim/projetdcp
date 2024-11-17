import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class RecipeService {
  private apiUrl = 'http://127.0.0.1:5000/recipes';

  constructor(private http: HttpClient) {}

  getRecipes(ingredients: string[]): Observable<any> {
    return this.http.post<any>(this.apiUrl, { ingredients });
  }
}