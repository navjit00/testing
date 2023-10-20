import os
from datetime import datetime, timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banking.db'  # Renamed to a more generic name
db = SQLAlchemy(app)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.String(10), nullable=False)
    category = db.Column(db.String(50), nullable=False)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    IBAN = db.Column(db.String(50), unique=True, nullable=False)

def add_demo_transactions():
    """Add 10 demo transactions to the database."""
    base_date = datetime.now()

    for i in range(10):
        date = (base_date - timedelta(days=i)).strftime('%Y-%m-%d')
        transaction = Transaction(
            date=date,
            amount=f"${(i + 1) * 10}",
            category="groceries" if i % 2 == 0 else "dining"
        )
        db.session.add(transaction)

    db.session.commit()

def add_demo_contacts():
    """Add demo contacts with IBANs to the database."""
    demo_contacts = [
        {"name": "Alice", "IBAN": "DE89370400440532013000"},
        {"name": "Bob", "IBAN": "FR7630006000011234567890189"},
        {"name": "Charlie", "IBAN": "GB33BUKB20201555555555"},
        {"name": "David", "IBAN": "ES9121000418450200051332"}
    ]

    for contact in demo_contacts:
        new_contact = Contact(name=contact["name"], IBAN=contact["IBAN"])
        db.session.add(new_contact)

    db.session.commit()

if __name__ == "__main__":
    # Delete the existing database file if it exists
    if os.path.exists("banking.db"):
        os.remove("banking.db")

    # Create a fresh database and tables
    with app.app_context():
        db.create_all()
        add_demo_transactions()
        add_demo_contacts()
