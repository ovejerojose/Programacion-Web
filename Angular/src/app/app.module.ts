import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http'; // Importa HttpClientModule

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './shared/header/header.component';
import { FooterComponent } from './shared/footer/footer.component';
import { PrincipalComponent } from './pages/principal/principal.component';
import { QuienessomosComponent } from './pages/quienessomos/quienessomos.component';
import { MapasitioComponent } from './pages/mapasitio/mapasitio.component';
import { FormularioComponent } from './pages/formulario/formulario.component';
import { AlquilarCanchaComponent } from './pages/alquilar-cancha/alquilar-cancha.component';
import { ServicioDePrueba } from './servicioDePrueba.service';
import { LoginComponent } from './auth/login/login.component';
import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    PrincipalComponent,
    QuienessomosComponent,
    MapasitioComponent,
    FormularioComponent,
    AlquilarCanchaComponent,
    LoginComponent
  
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule

  ],
  providers: [ServicioDePrueba],
  bootstrap: [AppComponent]
})
export class AppModule { }
