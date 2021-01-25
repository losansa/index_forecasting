from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:GqXyJf49rLQBZj0P@localhost:5432/index_forecasting'


from selling.controller import selling_routes


app.register_blueprint(selling_routes)
