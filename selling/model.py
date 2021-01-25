from app import db


class QuotesName(db.Model):
    __tablename__ = 'quotes_name'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    quotes = db.relationship('Quote', lazy='joined')


class Quote(db.Model):
    __tablename__ = 'quote'
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.String(80), nullable=False)
    q_open = db.Column(db.Float)
    q_high = db.Column(db.Float)
    q_low = db.Column(db.Float)
    q_adj_close = db.Column(db.Float)
    q_close = db.Column(db.Float)
    q_volume = db.Column(db.Float)
    q_name_id = db.Column(db.Integer,
                          db.ForeignKey('quotes_name.id', ondelete='CASCADE'),
                          nullable=False)
