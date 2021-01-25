from selling.model import QuotesName, Quote


def convert_quotes_names_to_dict(quotes_names):
    return list(map(convert_quote_name_to_dict, quotes_names))


def convert_quote_name_to_dict(quote_name: QuotesName):
    return {
        'id': quote_name.id,
        'name': quote_name.name
    }
    # dictionary['quotes'] = convert_quotes_to_dict(quote_name.quotes)
    # return dictionary


def convert_quotes_to_dict(quotes):
    return list(map(convert_quote_to_dict, quotes))


# def convert_quotes_to_dict(quotes):
#     arr = []
#     for quote in quotes:
#         arr.append(convert_quote_to_dict(quote))
#     return arr

def convert_quote_to_dict(quote: Quote):
    return {
        'id': quote.id,
        'quoteNameId': quote.q_name_id,
        'dateTime': quote.date_time,
        'open': quote.q_open,
        'high': quote.q_high,
        'low': quote.q_low,
        'adjClose': quote.q_adj_close,
        'close': quote.q_close,
        'volume': quote.q_volume,
    }
