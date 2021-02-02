import {Component, OnInit} from '@angular/core'
import {QuoteService} from 'src/app/quote/services/quote.service'
import {QuoteInterface} from 'src/app/quote/types/quote.interface'
import {ChartService} from 'src/app/quote/services/chart.service'

@Component({
  selector: 'app-quote-chart',
  templateUrl: './quote-chart.component.html',
  styleUrls: ['./quote-chart.component.scss'],
})
export class QuoteChartComponent implements OnInit {
  public quotes: QuoteInterface[] = []

  constructor(
    private chart: ChartService,
    private quoteService: QuoteService
  ) {}

  ngOnInit(): void {
    this.quoteService.fetch().subscribe((data: QuoteInterface[]) => {
      this.quotes = data

      this.updateCandlestick()
      this.updateColumn()
    })
  }

  updateCandlestick(): void {
    const sliceQuotes = this.quotes.slice(240, 310)
    this.chart.renderCandlestickChart('#candlestick')
    this.chart.updateCandlestickChart(sliceQuotes)
  }

  updateColumn(): void {
    const sliceQuotes = this.quotes.slice(240, 310)
    this.chart.renderColumnChart('#column')
    this.chart.updateColumnChart(sliceQuotes)
  }
}
