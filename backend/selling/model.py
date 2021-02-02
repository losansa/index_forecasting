from backend.app import db


class QuotesName(db.Model):
    __tablename__ = 'quotes_name'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


class Quote(db.Model):
    __tablename__ = 'quote'
    __table_args__ = {'extend_existing': True}
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
