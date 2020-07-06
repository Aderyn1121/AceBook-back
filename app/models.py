from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Instrument(db.Model):
    __tablename__ = 'instruments'
    id = db.Column(db.Integer, primary_key=True)
    date_bought = db.Column(db.Date, nullable=False)
    nickname = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer)
    maker = db.Column(db.String(50))
    type = db.Column(db.String(50), nullable=False)
    used = db.Column(db.Boolean, nullable=False)
