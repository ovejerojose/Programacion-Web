import { Component } from '@angular/core';
import { ServicioDePrueba } from '../../servicioDePrueba.service';

@Component({
  selector: 'app-alquilar-cancha',
  templateUrl: './alquilar-cancha.component.html',
  styleUrls: ['./alquilar-cancha.component.css']
})
export class AlquilarCanchaComponent {
  canchas: any[] = [];
  tipoCancha: string = '';
  nombreUsuario: string = '';
  emailUsuario: string = '';

  constructor(private servicioDePrueba: ServicioDePrueba) { }
  
  ngOnInit() {
    this.servicioDePrueba.obtenerCanchas().subscribe(
      (data: any) => {
        this.canchas = data;
      },
      (error) => {
        console.error(error); 
      }
    );
  }

  submitForm() {
    // Lógica para manejar el envío del formulario
  }
}


