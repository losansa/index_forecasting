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
      this.chart.renderChart('#candlestick')

      const sliceQuotes = this.quotes.splice(0, 100)

      this.chart.updateChart(sliceQuotes)
    })
  }
}
