import {Component, OnInit} from '@angular/core'
import {MenuItem} from 'primeng/api'

@Component({
  selector: 'app-main-layout',
  templateUrl: './main-layout.component.html',
  styleUrls: ['./main-layout.component.scss'],
})
export class MainLayoutComponent implements OnInit {
  public items: MenuItem[] = [
    {label: 'Главная', icon: 'pi pi-fw pi-home'},
    {label: 'Таблица', icon: 'pi pi-fw pi-table', routerLink: '/quote'},
    {label: 'График', icon: 'pi pi-fw pi-chart-bar'},
  ]

  constructor() {}

  ngOnInit() {}
}
