import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PrincipalComponent } from './pages/principal/principal.component';
import { QuienessomosComponent } from './pages/quienessomos/quienessomos.component';
import { MapasitioComponent } from './pages/mapasitio/mapasitio.component';
import { FormularioComponent } from './pages/formulario/formulario.component';
import { AlquilerComponent } from './pages/alquiler/alquiler.component';
import { TiendaComponent } from './pages/tienda/tienda.component';
import { LoginComponent } from './auth/login/login.component';
import { TorneosComponent } from './pages/torneos/torneos.component';

// rutas es un arreglo [], linkea el modulo con el path que se usa en lugar del href
//      Del link a index.html se cambiar a routerLink="index"
//      <li><a href="index.html">Inicio</a></li>
//      <li><a routerLink="index">Inicio</a></li>

const app_routes: Routes = [
  //Link genericos para que ante error vaya al principal
  { path: '', component: PrincipalComponent},
  //{ path: '**', pathMatch: 'full', redirectTo: ''},
  //Links del nav
  { path: 'inicio', component: PrincipalComponent},
  { path: 'alquiler', component: AlquilerComponent},
  { path: 'torneos', component: TorneosComponent},
  { path: 'tienda', component: TiendaComponent},
  //Link usuarios
  { path: 'login', component: LoginComponent},
  { path: 'formulario', component: FormularioComponent},
  //Links del footer
  { path: 'mapasitio', component: MapasitioComponent},
  { path: 'quienessomos', component: QuienessomosComponent}
  ];


//decorador? vaya a saber que es esto
@NgModule({
  imports: [RouterModule.forRoot(app_routes)],
  exports: [RouterModule]
})

// defino clase
export class AppRoutingModule { }
