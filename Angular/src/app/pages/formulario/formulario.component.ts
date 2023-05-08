import { Component } from '@angular/core';
import {Router} from '@angular/router';
import { LoginService } from 'src/app/services/auth/login.service';
import { FormBuilder, Validators } from '@angular/forms';


@Component({
  selector: 'app-formulario',
  templateUrl: './formulario.component.html',
  styleUrls: ['./formulario.component.css']
})


export class FormularioComponent {


  RegisterForm = this.formBuilder.group({
    email:['cualquiera@gmail.com',[Validators.required, Validators.email]], //forms control 
    password:['', Validators.required]
  })

  
  constructor(private formBuilder:FormBuilder, private router:Router, private loginService: LoginService) {}

  get email(){
    return this.RegisterForm.controls.email;
  }
  get password(){
    return this.RegisterForm.controls.password;
  }

registrarusuario(){
  alert("Felicitaciones, te has registrado con exito")
  this.router.navigateByUrl('/inicio');
}

}




