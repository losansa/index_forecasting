import {NgModule} from '@angular/core'
import {SharedModule} from 'src/app/shared/modules/shared.module'
import {QuoteTableComponent} from 'src/app/quote/components/quote-table/quote-table.component'
import {RouterModule, Routes} from '@angular/router'
import {QuoteChartComponent} from './components/quote-chart/quote-chart.component'

const routes: Routes = [
  {path: 'table', component: QuoteTableComponent},
  {path: 'chart', component: QuoteChartComponent},
]

@NgModule({
  declarations: [QuoteTableComponent, QuoteChartComponent],
  imports: [SharedModule, RouterModule.forChild(routes)],
})
export class QuoteModule {}
