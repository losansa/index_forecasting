from flask import Blueprint, request
from flask.json import jsonify

from selling import repository, serializer


selling_routes = Blueprint('hello', __name__)


@selling_routes.route('/quote-name')
def get_all_quotes_names():
    all_quote_names = repository.get_all_quotes_names()
    return jsonify(serializer.convert_quotes_names_to_dict(all_quote_names))


@selling_routes.route('/quote')
def get_all_quotes():
    filtered_quotes = repository.get_filtered_quotes(request.args.get('quoteId'))
    return jsonify(serializer.convert_quotes_to_dict(filtered_quotes))
