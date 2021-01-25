from database import db
from selling.model import QuotesName, Quote


def get_all_quotes_names():
    query = db.session.query(QuotesName)  # SELECT * FROM public.quotes_name
    return query.all()


def get_filtered_quotes(quote_name_id):
    query = db.session.query(Quote)  # SELECT * FROM public.quotes_name
    query = query.filter(Quote.q_name_id == quote_name_id)  # SELECT * FROM public.quotes_name
    return query.all()
