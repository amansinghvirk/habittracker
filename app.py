import os
from flask import Flask
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def mongo_string():
    return os.getenv("MONGODB_URI")

def habittracker_db():
    client = MongoClient(mongo_string())
    db = client.habittracker
    return db

def create_app():
    app = Flask(__name__)
    app.db = habittracker_db()
    app.register_blueprint(pages)
    
    return app