import {Component} from '@angular/core'
import {MenuItem, PrimeNGConfig} from 'primeng/api'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  public items: MenuItem[] = [
    {label: 'Главная', icon: 'pi pi-fw pi-home'},
    {label: 'Таблица', icon: 'pi pi-fw pi-table', routerLink: '/table'},
    {label: 'График', icon: 'pi pi-fw pi-chart-bar', routerLink: '/chart'},
  ]

  constructor(private primengConfig: PrimeNGConfig) {}

  ngOnInit() {
    this.primengConfig.ripple = true
  }
}
