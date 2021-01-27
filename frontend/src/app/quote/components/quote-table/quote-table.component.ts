import {Component, OnInit} from '@angular/core'
import {QuoteService} from 'src/app/quote/services/quote.service'
import {QuoteInterface} from 'src/app/quote/types/quote.interface'

@Component({
  selector: 'app-quote-layout',
  templateUrl: './quote-table.component.html',
  styleUrls: ['./quote-table.component.scss'],
})
export class QuoteTableComponent implements OnInit {
  public quotes: QuoteInterface[] = []

  constructor(private quoteService: QuoteService) {}

  ngOnInit(): void {
    this.quoteService.fetch().subscribe((data: QuoteInterface[]) => {
      this.quotes = data
    })
  }
}
