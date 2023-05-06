import { Injectable } from '@angular/core';
import { LoginRequest } from './loginRequest';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, catchError, throwError, BehaviorSubject, tap } from 'rxjs';
import { User } from './user';

//todo servicio tiene decorador un injectable
@Injectable({
  providedIn: 'root',
})
export class LoginService {
  //creo dos instancia, BehaviorSubjects 
  currentUserLoginOn: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false);
  currentUserData: BehaviorSubject<User> = new BehaviorSubject<User>({id: 0,email: '',});

  constructor(private http: HttpClient) {}

  //creo metodo login despues de va a comunicar con la api-rest
  // any es tipo de datos generico
  login(credentials: LoginRequest): Observable<User> {
    //console.log(credentials);
    //agrego operador tap
    //el metodo get devuelve como tipo de dato 'user'
    //operador pipe permite encadenar servicios
    //tap acciones adicionales , no modifica la secuciencia de los observables
    return this.http.get<User>('././assets/data.json').pipe(
      tap((userData: User) => {
        this.currentUserData.next(userData);
        this.currentUserLoginOn.next(true);
      }),
      catchError(this.handleError)
    );
  }
  //configurador de manejador del error para peticiones http

  //recibe por parametro un error
  //recibe codigo de estado del backend
  //mal formulado el request o 
  //status == 0 que no devolvio codigo de estado
  private handleError(error: HttpErrorResponse) {
    if (error.status == 0) {
      console.error('Se ha producido un error ', error.error);
    } else {
      console.error(
        'Backendo retornó el código de estado ',
        error.status,
        error.error
      );
    }
    return throwError(
      () => new Error('Algo falló. Por favor intente nuevamente.')
    );
  }
  // :Observable es el tipo de valor que devuelve
  get userData():Observable<User>{  
    return this.currentUserData.asObservable();
  }

get userLoginOn():Observable<boolean>{
  return this.currentUserLoginOn.asObservable();
}

}
