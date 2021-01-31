from backend.app import db
from selling.model import QuotesName, Quote


def get_all_quotes_names():
    query = db.session.query(QuotesName)
    return query.all()


def get_all_quotes():
    query = db.session.query(Quote)
    return query.all()


def get_filtered_quotes(quote_name_id):
    query = db.session.query(Quote)
    query = query.filter(Quote.q_name_id == quote_name_id)
    return query.all()


def get_quote_closes_values():
    query = db.session.query(Quote.q_close)
    query = query.filter(Quote.q_name_id == 1)
    return query.all()
