import json
from models import Transaction

def get_all_transactions():
    transactions = Transaction.query.all()
    output = []
    for transaction in transactions:
        transaction_data = {}
        transaction_data['id'] = transaction.id
        transaction_data['date'] = transaction.date
        transaction_data['amount'] = transaction.amount
        transaction_data['category'] = transaction.category
        output.append(transaction_data)
    return json.dumps(output)