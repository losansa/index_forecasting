from selling import repository


def get_all_quotes_names():
    return repository.get_all_quotes_names()


def get_filtered_quotes(quote_name_id):
    if quote_name_id:
        quotes = repository.get_filtered_quotes(quote_name_id)
    else:
        quotes = repository.get_all_quotes()
    return quotes
