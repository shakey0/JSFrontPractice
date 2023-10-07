import os
from flask import Flask, request, redirect, render_template, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.jinja_env.autoescape = True


class TestData:

    def __init__(self, name, is_it, tags):
        self.name = name
        self.is_it = is_it
        self.tags = tags


@app.route("/")
def home():
    test_items = [TestData("James", True, ["art", "music", "drama", "maths"]),
                TestData("Toby", True, ["English", "history", "drama"]),
                TestData("Michelle", False, ["music", "drama", "PE"]),
                TestData("Sophie", True, ["art", "science", "geography", "design"]),
                TestData("Liz", False, ["art", "English", "maths", "science", "design"]),
                TestData("Thomas", False, ["history", "geography"]),
                TestData("Jodie", True, ["PE"])]
    return render_template("index.html", test_items=test_items)


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))