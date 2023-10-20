from flask import request, jsonify, make_response
import openai
from app import app, db
from models import Transaction
from utils import get_all_transactions

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
    user_message = data['userMessage']

    messages = [
        {"role": "system", "content": "You are a helpful banking app assistant."},
        {"role": "user", "content": user_message}
    ]

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

            if not name and not IBAN:
                bot_reply = "Please provide the name and IBAN for the contact."
                return jsonify(botReply=bot_reply)
            
            if not IBAN:
                # If IBAN is missing, ask the user for it
                bot_reply = "Please provide the IBAN for the contact named {}.".format(name)
                return jsonify(botReply=bot_reply)

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


@app.route('/create-contact', methods=['POST'])
def create_contact():
    data = request.json
    name = data['name']
    IBAN = data['IBAN']

    # Check if IBAN already exists in the database to avoid duplication
    existing_contact = Contact.query.filter_by(IBAN=IBAN).first()
    if existing_contact:
        return jsonify(success=False, message="Contact with this IBAN already exists!")

    new_contact = Contact(name=name, IBAN=IBAN)
    db.session.add(new_contact)
    db.session.commit()

    return jsonify(success=True, message="Contact created successfully!")