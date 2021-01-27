import {NgModule} from '@angular/core'
import {TableModule} from 'primeng/table'
import {CardModule} from 'primeng/card'
import {MenubarModule} from 'primeng/menubar'
import {TabMenuModule} from 'primeng/tabmenu'

@NgModule({
  imports: [TableModule, CardModule, MenubarModule, TabMenuModule],
  exports: [TableModule, CardModule, MenubarModule, TabMenuModule],
})
export class PrimeNgModule {}
