import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import {Router} from '@angular/router';
import { LoginService } from 'src/app/services/auth/login.service';
import { LoginRequest } from 'src/app/services/auth/loginRequest';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

parrafoLoginError:string=""

/*
Aca creo el objeto formulario con el servicio de formBuilder
le pongo algunos valores por defecto
En el html a la etiqueta form debo ponerle agregarle [formGroup]="loginForm" para enlazar 
este objeto con lo que tiene el html
En el html a la etiqueta imput le debo poner formControlName="email" para asociarlo al imput 
que es para completar el email y al password formControlName="password"
*/
/*
Aca tambien voy a crear las validaciones para el formulario

         este es el valor             aca son las dos validaciones sincronicas
         por defecto                  que le pongo al campo email          
email:['cualquiera@gmail.com',[Validators.required, Validators.email]]

Para que funciones tengo que agregar la clase validator
import { FormBuilder, Validators } from '@angular/forms';

*/

loginForm = this.formBuilder.group({
  email:['cualquiera@gmail.com',[Validators.required, Validators.email]], //forms control 
  password:['', Validators.required]
})

/*
injeccion del servicio de Rutas
private router:Router para que luego del hacer el login
la pagina vaya a la pagina de inicio
*/
constructor(private formBuilder:FormBuilder, private router:Router, private loginService: LoginService) {}

get email(){
  return this.loginForm.controls.email;
}
get password(){
  return this.loginForm.controls.password;
}


log2(){
  if(this.loginForm.valid){    //pregunto si el formulario es valido
    //console.log("llamar al servicio de login");
    alert("Funciona");

    this.router.navigateByUrl('/inicio'); // me manda al inicio
    this.loginForm.reset(); //borra los datos
      }    // cierra el if es valido
  else {  //si no es valido el formulario mando una mensaje/alerta (tipo pop up)
  alert("Error al ingresar los datos.");
  }   //cierra el else

}


/*
En los formularios reactivos tengo que crear un metodo para que cuando hago clic en 
el boton de iniciar sesion haga algo 
Es metodo es el login(), cuando haga clic en el boton lo llama

En el html enlazo el metodo con el click=nombre del metodo
 <button type="submit" (click)="login()" class="btn btn-primary">

alert -> tira el mensaje por pantalla
console -> tira el mensaje en la consola del navegador


*/

login(){
  if(this.loginForm.valid){    //pregunto si el formulario es valido
    //console.log("llamar al servicio de login");
    alert("Funciona");
    this.loginService.login(this.loginForm.value as LoginRequest).subscribe({
      next: (userData) => {
        console.log(userData);
      },
      error: (errorData) => {
        console.error(errorData);
        this.parrafoLoginError=errorData;
      },
      complete: () => {
        console.info("Login completo");
        this.router.navigateByUrl('/inicio');
        this.loginForm.reset();
      }        
      
    });

  }    // cierra el if es valido
  else {  //si no es valido el formulario mando una mensaje/alerta (tipo pop up)
  alert("Error al ingresar los datos.");
  this.loginForm.markAllAsTouched();
  }   //cierra el else

}   //cierra metodo login

//metodo registrate
registrate(){
  this.router.navigateByUrl('formulario');
}

}


