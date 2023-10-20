from app import db

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(15), nullable=False)
    amount = db.Column(db.String(10), nullable=False)
    category = db.Column(db.String(50), nullable=False)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    IBAN = db.Column(db.String(50), unique=True, nullable=False)