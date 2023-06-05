import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PrincipalComponent } from './pages/principal/principal.component';
import { QuienessomosComponent } from './pages/quienessomos/quienessomos.component';
import { MapasitioComponent } from './pages/mapasitio/mapasitio.component';
import { FormularioComponent } from './pages/formulario/formulario.component';
import { AlquilarCanchaComponent } from './pages/alquilar-cancha/alquilar-cancha.component';
import { LoginComponent } from './auth/login/login.component';

//creo constante tipo Routes ?¿

// rutas es un arrelo []
const app_routes: Routes = [
  { path: 'inicio', component: PrincipalComponent },
  { path: 'quienessomos', component: QuienessomosComponent },
  { path: 'mapasitio', component: MapasitioComponent },
  { path: 'formulario', component: FormularioComponent },
  { path: 'alquilar-cancha', component: AlquilarCanchaComponent },
  { path: 'iniciar-sesion', component:LoginComponent },
  { path: '**', pathMatch: 'full', redirectTo: '' }
 
];



//decorador? vaya a saber que es esto
@NgModule({
  imports: [RouterModule.forRoot(app_routes)],
  exports: [RouterModule]
})

// defino clase
export class AppRoutingModule { }
