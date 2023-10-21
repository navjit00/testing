from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import config
import openai  # Import the library
import os

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
CORS(app)

from routes import *

if __name__ == "__main__":
    app.run(debug=True, port=5001)
