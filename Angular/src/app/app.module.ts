import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './shared/header/header.component';
import { FooterComponent } from './shared/footer/footer.component';
import { PrincipalComponent } from './pages/principal/principal.component';
import { QuienessomosComponent } from './pages/quienessomos/quienessomos.component';
import { MapasitioComponent } from './pages/mapasitio/mapasitio.component';
import { FormularioComponent } from './pages/formulario/formulario.component';
import { TiendaComponent } from './pages/tienda/tienda.component';
import { AlquilerComponent } from './pages/alquiler/alquiler.component';
import { TorneosComponent } from './pages/torneos/torneos.component';
import { LoginComponent } from './auth/login/login.component';
import { NavComponent } from './shared/nav/nav.component';
import { ReactiveFormsModule} from '@angular/forms';
import { HttpClientModule} from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    PrincipalComponent,
    QuienessomosComponent,
    MapasitioComponent,
    FormularioComponent,
    TiendaComponent,
    AlquilerComponent,
    TorneosComponent,
    LoginComponent,
    NavComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
