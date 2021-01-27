import {NgModule} from '@angular/core'
import {RouterModule, Routes} from '@angular/router'
import {MainLayoutComponent} from 'src/app/shared/components/main-layout/main-layout.component'

const routes: Routes = [
  {
    path: '',
    component: MainLayoutComponent,
    children: [
      {
        path: 'quote',
        loadChildren: () =>
          import('./quote/quote.module').then((m) => m.QuoteModule),
      },
    ],
  },
]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
