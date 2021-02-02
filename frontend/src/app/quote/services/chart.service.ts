import {Injectable} from '@angular/core'
import {
  QuoteChartInterface,
  QuoteInterface,
} from 'src/app/quote/types/quote.interface'

declare let ApexCharts: any

@Injectable({
  providedIn: 'root',
})
export class ChartService {
  private chart: any

  renderChart(selector: string): void {
    this.chart = new ApexCharts(document.querySelector(selector), {
      series: [
        {
          data: [],
        },
      ],
      chart: {
        type: 'candlestick',
        height: 350,
      },
      title: {
        text: 'Квоты',
        align: 'left',
      },
      xaxis: {
        type: 'datetime',
      },
      yaxis: {
        tooltip: {
          enabled: true,
        },
      },
    })
    this.chart.render()
  }

  updateChart(list: QuoteInterface[]): void {
    this.chart.updateOptions({
      series: [
        {
          data: this.getChartData(list),
        },
      ],
    })
  }

  private getChartData(quotes: QuoteInterface[]): QuoteChartInterface[] {
    return quotes.map((quote) => {
      return {
        x: new Date(quote.dateTime),
        y: [quote.open, quote.high, quote.low, quote.close],
      }
    })
  }
}
