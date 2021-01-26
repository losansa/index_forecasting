import {NgModule} from '@angular/core'
import {TableModule} from 'primeng/table'
import {CardModule} from 'primeng/card'
import {MenubarModule} from 'primeng/menubar'

@NgModule({
  imports: [TableModule, CardModule, MenubarModule],
  exports: [TableModule, CardModule, MenubarModule],
})
export class PrimeNgModule {}
