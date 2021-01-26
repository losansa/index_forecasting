import {Component, OnInit} from '@angular/core'
import {QuoteService} from 'src/app/quote/services/quote.service'
import {QuoteInterface} from 'src/app/quote/types/quote.interface'

@Component({
  selector: 'app-quote-layout',
  templateUrl: './quote-layout.component.html',
  styleUrls: ['./quote-layout.component.scss'],
})
export class QuoteLayoutComponent implements OnInit {
  public quotes: QuoteInterface[] = []

  constructor(private quoteService: QuoteService) {}

  ngOnInit(): void {
    this.quoteService.fetch().subscribe((data: QuoteInterface[]) => {
      this.quotes = data
    })
  }
}
