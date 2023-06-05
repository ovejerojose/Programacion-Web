import { Injectable } from '@angular/core';
import { LoginRequest } from './loguinRequest';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, catchError, throwError } from 'rxjs';
import { User } from './user';
@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private http: HttpClient) { }

  login(credentials:LoginRequest):Observable<User>{
   return this.http.get<User>('https://my-json-server.typicode.com/ariel957/ariel957-JsonCanchas/users').pipe(
    catchError(this.handleError)
   )
  }
  private handleError(error:HttpErrorResponse){
    if(error.status ===0){
      console.error('Se ha producido un error',error.error);
    }
    else{
      console.error('Backend retorno el codigo de estado',error.status,error.error);
    }
    return throwError(()=> new Error('Algo fallo.Por favor intente nuevamente'))
  }
}
