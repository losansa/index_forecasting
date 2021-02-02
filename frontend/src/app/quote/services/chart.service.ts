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
  private candlestickChart: any
  private columnChart: any

  renderColumnChart(selector: string): void {
    this.columnChart = new ApexCharts(document.querySelector(selector), {
      series: [
        {
          name: 'Net Profit',
          data: [],
        },
      ],
      chart: {
        type: 'bar',
        height: 350,
        brush: {
          enabled: true,
          target: 'candles',
        },
      },
      plotOptions: {
        bar: {
          horizontal: false,
          columnWidth: '55%',
          endingShape: 'rounded',
        },
      },
      dataLabels: {
        enabled: false,
      },
      stroke: {
        show: true,
        width: 2,
        colors: ['transparent'],
      },
      xaxis: {
        categories: [],
      },
      yaxis: {
        title: {
          text: '$ (thousands)',
        },
      },
      fill: {
        opacity: 1,
      },
    })
    this.columnChart.render()
  }

  renderCandlestickChart(selector: string): void {
    this.candlestickChart = new ApexCharts(document.querySelector(selector), {
      series: [
        {
          data: [],
        },
      ],
      chart: {
        type: 'candlestick',
        height: 350,
        id: 'candles',
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
    this.candlestickChart.render()
  }

  updateColumnChart(list: QuoteInterface[]): void {
    this.columnChart.updateOptions({
      series: [
        {
          data: this.getColumnChartData(list),
        },
      ],
    })
  }

  updateCandlestickChart(list: QuoteInterface[]): void {
    this.candlestickChart.updateOptions({
      series: [
        {
          data: this.getCandlestickChartData(list),
        },
      ],
    })
  }

  private getColumnChartData(quotes: QuoteInterface[]): any[] {
    return quotes.map((quote) => {
      return {
        x: new Date(quote.dateTime).getTime(),
        y: quote.volume,
      }
    })
  }

  private getCandlestickChartData(
    quotes: QuoteInterface[]
  ): QuoteChartInterface[] {
    return quotes.map((quote) => {
      return {
        x: new Date(quote.dateTime).getTime(),
        y: [quote.open, quote.high, quote.low, quote.close],
      }
    })
  }
}
