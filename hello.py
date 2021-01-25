from flask import Blueprint

# импортируем репозиторий и сериализатор

route_registrator = Blueprint('hello', __name__)


@route_registrator.route('/')
def hello_world():
    # получаем данные из репозитория
    # сериализуем в json
    return 'Hello, World! help'
