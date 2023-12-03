import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


@app.route("/wave", methods=["GET"])
def get_wave():
    name = request.args.get("name")
    return f"I am waving at {name}"


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    message = request.form["message"]
    return f'Thanks {name}, you sent this message: "{message}"'


@app.route("/count_vowels", methods=["POST"])
def count_vowels():
    text = request.form.get("text")
    vowel_counter = sum(1 for char in text if char in "aeiouAEIOU")
    return f'There are {vowel_counter} vowels in "{text}"'


@app.route("/sort-names", methods=["POST"])
def sort_names():
    names = request.form.get("names")
    return ",".join(sorted(names.split(",")))


name_list = ["Alice", "Julia", "Karim"]


@app.route("/names", methods=["GET"])
def add_names():
    new_name = request.args.get("add")
    for name in new_name.split(","):
        name_list.append(name)
    return ", ".join(sorted(name_list))


# == End Example Code ==

if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))
