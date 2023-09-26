from flask import Flask, render_template
from flask_navigation import Navigation

app = Flask(__name__)
nav = Navigation(app)

@app.route("/")
def index():
    return "Current Inventory"

@app.route("/add")
def add():
    return "Add Inventory"

if __name__ == "__main__":
    app.run(debug=True)