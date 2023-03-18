"""
Flask application
This module contains functions for performing various tasks.
"""
from flask import Flask, render_template, request

main = Flask(__name__)


@main.route("/")
def hello_world():
    """
    Displays a simple greeting message, that returns a string containing the message "Hello World!".
    """
    return "Hello World!"

@main.route("/hello", methods=["GET", "POST"])
def hello():
    """
    Displays a form to enter a name and greets the user.
    """
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"
    return render_template("index.html")


if __name__ == "__main__":
    main.run(debug=True, host='0.0.0.0', port=8000)