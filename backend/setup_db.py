import os
from datetime import datetime, timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Go up one directory from BASE_DIR, then down into 'instance'
db_path = os.path.join(BASE_DIR, '..', 'instance', 'banking.db')

# Convert the path to an absolute path (this will resolve the '..')
db_path = os.path.abspath(db_path)

print(db_path)

# Set the SQLAlchemy Database URI using an absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
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

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(10), nullable=False)

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
        # Check if a contact with the same IBAN already exists
        existing_contact = Contact.query.filter_by(IBAN=contact["IBAN"]).first()
        if existing_contact is None:
            new_contact = Contact(name=contact["name"], IBAN=contact["IBAN"])
            db.session.add(new_contact)

    db.session.commit()



def add_demo_history():
    """Add demo history entries to the database."""
    demo_history = [
        {"message": "User logged in", "type": "user"},
        {"message": "System update performed", "type": "system"},
        {"message": "New transaction added", "type": "user"}
    ]

    for entry in demo_history:
        # Check if the history entry already exists
        existing_history = Message.query.filter_by(message=entry["message"], type=entry["type"]).first()
        if existing_history is None:
            new_history =  Message(message=entry["message"], type=entry["type"])
            db.session.add(new_history)

    db.session.commit()

if __name__ == "__main__":
    # Delete the existing database file if it exists
  # Check if the file exists and remove it
    if os.path.exists(db_path):
        os.remove(db_path)
        print("Database file removed.")
    else:
        print("Database file does not exist.")

    # Create a fresh database and tables
    with app.app_context():
        db.create_all()
        add_demo_transactions()
        add_demo_contacts()
      #  add_demo_history()
