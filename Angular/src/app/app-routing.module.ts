import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PrincipalComponent } from './pages/principal/principal.component';
import { QuienessomosComponent } from './pages/quienessomos/quienessomos.component';
import { MapasitioComponent } from './pages/mapasitio/mapasitio.component';
import { FormularioComponent } from './pages/formulario/formulario.component';

//creo constante tipo Routes ?¿

// rutas es un arrelo []
const app_routes: Routes = [
  { path: '', component: PrincipalComponent},
  { path: 'quienessomos', component: QuienessomosComponent},
  { path: 'mapasitio', component: MapasitioComponent},
  { path: 'formulario', component: FormularioComponent},
  { path: '**', pathMatch: 'full', redirectTo: ''}
];


//decorador? vaya a saber que es esto
@NgModule({
  imports: [RouterModule.forRoot(app_routes)],
  exports: [RouterModule]
})

// defino clase
export class AppRoutingModule { }
