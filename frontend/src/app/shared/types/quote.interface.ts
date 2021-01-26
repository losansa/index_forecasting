export interface QuoteInterface {
  adjClose: number // Цена последней закрытой сделки
  close: number // Цена закрытия
  dateTime: Date // Дата(время) обновления
  high: number // Самая высокая цена
  id?: number //
  low: number // Самая низкая цена
  open: number // Цена открытия
  quoteNameId: number // Ссылка на дропдаун
  volume: number // Объем просто
}
