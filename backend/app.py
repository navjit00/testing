from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import config
import openai  # Import the library


app = Flask(__name__)
app.config.from_object(config.Config)
openai.api_key = app.config['OPENAI_API_KEY']

db = SQLAlchemy(app)
CORS(app)

from routes import *

if __name__ == "__main__":
    app.run(debug=True, port=5001)
