from flask import request, jsonify, make_response
import openai
from app import app, db
from models import Transaction,Message,Contact
from utils import get_all_transactions
from enum import Enum
from sqlalchemy import asc



class HistoryTypes(Enum):
    user = 'user'
    system = 'system'

@app.route('/message', methods=['POST', 'OPTIONS'])
def get_bot_reply():
    if request.method == 'OPTIONS':
        app.logger.info('Received OPTIONS request')
        response = make_response()
        response.headers["Access-Control-Allow-Origin"] = "*"  # Allow all origins
        response.headers["Access-Control-Allow-Methods"] = "POST"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response

    data = request.json
    user_message_content = data['userMessage']

    messages = [{"role": "system", "content": "You are a helpful banking app assistant."}]

    # Retrieve all previous messages from the database and add them to the list
    saved_messages = Message.query.order_by(asc(Message.id)).all()
    for msg in saved_messages:
        role = "user" if msg.type == HistoryTypes.user.value else "system"
        messages.append({"role": role, "content": msg.message})

    # Add the current user message
    messages.append({"role": "user", "content": user_message_content})

    # Save user message to the database
    user_message = Message(message=user_message_content, type='user')
    db.session.add(user_message)
    db.session.commit()

    functions = [
        {
            "name": "get_all_transactions",
            "description": "Retrieve all banking transactions",
            "parameters": {
                "type": "object",
                "properties": {}  # Explicitly defining an empty properties object
            }
        },
        {
            "name": "create_contact",
            "description": "Create a new contact with a name and IBAN",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "IBAN": {"type": "string"}
                },
                "required": ["name", "IBAN"]
            }
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto",
    )
    response_message = response["choices"][0]["message"]

    # Check for function calls
    if response_message.get("function_call"):
        function_name = response_message["function_call"]["name"]

        if function_name == "get_all_transactions":
            function_response = get_all_transactions()

            messages.append(response_message)
            messages.append(
                {
                    "role": "function",
                    "name": function_name,
                    "content": function_response,
                }
            )

        elif function_name == "create_contact":
        # Check if "parameters" key exists, if not, initialize as empty dict
            function_params = response_message["function_call"].get("parameters", {})

            # Extract the provided name and IBAN, if available
            name = function_params.get("name")
            IBAN = function_params.get("IBAN")
            
           
            function_response = create_contact()

            messages.append(response_message)
            messages.append(
                {
                    "role": "function",
                    "name": function_name,
                    "content": function_response,
                }
            )
            second_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613",
                messages=messages,
            )
            bot_reply = second_response["choices"][0]["message"]["content"].strip()
    else:
        bot_reply = response_message["content"].strip()

    system_message = Message(message=bot_reply, type='system')
    db.session.add(system_message)
    db.session.commit()
    return jsonify(botReply=bot_reply)


@app.route('/get-transactions', methods=['GET'])
def get_transactions():
    # Query the database for all transactions
    transactions = Transaction.query.all()
    
    # Convert transactions to a list of dictionaries
    output = []
    for transaction in transactions:
        transaction_data = {}
        transaction_data['id'] = transaction.id
        transaction_data['date'] = transaction.date
        transaction_data['amount'] = transaction.amount
        transaction_data['category'] = transaction.category
        output.append(transaction_data)
    
    return output



@app.route('/get-messages', methods=['GET'])
def get_messages():
    # Query the database for all history entries
    history_entries = Message.query.all()
    
    # Convert history entries to a list of dictionaries
    output = []
    for entry in history_entries:
        entry_data = {}
        entry_data['id'] = entry.id
        entry_data['message'] = entry.message
        entry_data['type'] = entry.type
        output.append(entry_data)
    
    return jsonify(output)

@app.route('/create-message', methods=['POST'])
def create_message():
    data = request.json
    message = data['message']
    type = data['type']

    new_message = Message(message=message, type=type)
    db.session.add(new_message)
    db.session.commit()

    return jsonify(success=True, message="Message entry added successfully!")


@app.route('/delete-messages', methods=['DELETE'])
def delete_messages():
    try:
        Message.query.delete()
        db.session.commit()
        return jsonify(success=True, message="All messages deleted successfully!")
    except Exception as e:
        db.session.rollback()
        return jsonify(success=False, message=str(e)), 500