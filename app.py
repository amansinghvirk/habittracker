import os
import datetime
from flask import Flask, render_template, request


def date_range(start: datetime.date):
    dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
    return dates


def create_app():
    app = Flask(__name__)

    habits = ["Test habit", "Test habit 2"]

    @app.route('/')
    def index():
        date_str = request.args.get("date")
        if date_str:
            selected_date = datetime.date.fromisoformat(date_str)
        else:
            selected_date = datetime.date.today()

        return render_template(
            "index.html", 
            habits=habits, 
            title="Habit Tracker - Home",
            date_range=date_range,
            selected_date=selected_date
        )
    
    @app.route("/add", methods=["GET", "POST"])
    def add_habit():
        if request.method == "POST":
            habit = request.form.get("habit")
            habits.append(habit)
        return render_template("add_habit.html", title="Habit Tracker - Add Habit")

    return app