import {NgModule} from '@angular/core'
import {SharedModule} from 'src/app/shared/modules/shared.module'
import {QuoteLayoutComponent} from './components/quote-layout/quote-layout.component'
import {RouterModule, Routes} from '@angular/router'

const routes: Routes = [{path: '', component: QuoteLayoutComponent}]

@NgModule({
  declarations: [QuoteLayoutComponent],
  imports: [SharedModule, RouterModule.forChild(routes)],
})
export class QuoteModule {}
