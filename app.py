import os
import datetime
from flask import Flask, render_template, request

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template("index.html", title="Habit Tracker - Home")
    
    @app.route("/add", methods=["GET", "POST"])
    def add_habit():
        return render_template("add_habit.html", title="Habit Tracker - Add Habit")

    return app