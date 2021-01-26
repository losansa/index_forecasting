import {Injectable} from '@angular/core'
import {HttpClient} from '@angular/common/http'
import {Observable} from 'rxjs'
import {QuoteInterface} from 'src/app/shared/types/quote.interface'

@Injectable({
  providedIn: 'root',
})
export class QuoteService {
  constructor(private http: HttpClient) {}

  fetch(): Observable<QuoteInterface[]> {
    return this.http.get<QuoteInterface[]>('/api/quote')
  }
}
