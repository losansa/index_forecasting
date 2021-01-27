import {NgModule} from '@angular/core'
import {RouterModule, Routes} from '@angular/router'
import {BrowserModule} from '@angular/platform-browser'
import {BrowserAnimationsModule} from '@angular/platform-browser/animations'

import {AppComponent} from './app.component'
import {QuoteModule} from 'src/app/quote/quote.module'
import {SharedModule} from 'src/app/shared/modules/shared.module'

const routes: Routes = [{path: '', redirectTo: '/table', pathMatch: 'full'}]

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    RouterModule.forRoot(routes),
    SharedModule,
    QuoteModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
