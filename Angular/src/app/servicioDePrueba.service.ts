import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class ServicioDePrueba {

  constructor(private http: HttpClient) { }

  public obtenerCanchas() {
    return this.http.get('https://my-json-server.typicode.com/ariel957/ariel957-JsonCanchas/canchas');
  }
}
