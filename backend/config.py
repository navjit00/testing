import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///banking.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = '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'