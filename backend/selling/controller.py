from flask import Blueprint, request
from flask.json import jsonify

from selling import service, serializer


selling_routes = Blueprint('hello', __name__)


@selling_routes.route('/quote-name')
def get_all_quotes_names():
    all_quote_names = service.get_all_quotes_names()
    return jsonify(serializer.convert_quotes_names_to_dict(all_quote_names))


@selling_routes.route('/quote')
def get_all_quotes():
    quote_id = request.args.get('quoteId')
    filtered_quotes = service.get_filtered_quotes(quote_id)
    return jsonify(serializer.convert_quotes_to_dict(filtered_quotes))
