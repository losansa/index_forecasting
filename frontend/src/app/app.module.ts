import {NgModule} from '@angular/core'
import {BrowserModule} from '@angular/platform-browser'
import {BrowserAnimationsModule} from '@angular/platform-browser/animations'

import {AppComponent} from './app.component'
import {AppRoutingModule} from './app-routing.module'
import {SharedModule} from 'src/app/shared/modules/shared.module'
import {QuoteModule} from 'src/app/quote/quote.module';
import { MainLayoutComponent } from './shared/components/main-layout/main-layout.component'

@NgModule({
  declarations: [AppComponent, MainLayoutComponent],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    SharedModule,
    QuoteModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
