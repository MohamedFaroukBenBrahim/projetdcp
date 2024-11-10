import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavComponent } from './nav/nav.component';
import { FooterComponent } from './footer/footer.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { RecpiesComponent } from './recpies/recpies.component';
import { RouterModule,Routes } from '@angular/router';
import { FormsModule } from '@angular/forms';
const routes: Routes = [
  {path : "" ,component : WelcomeComponent},
  {path : "welcome" , component : WelcomeComponent},
  {path : "recipes" , component : RecpiesComponent}
];
@NgModule({
  declarations: [
    AppComponent,
    NavComponent,
    FooterComponent,
    WelcomeComponent,
    RecpiesComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    RouterModule.forRoot(routes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
