from flask import Flask, render_template
from flask import jsonify
from json import *

app = Flask(__name__, static_folder="../static/dist", template_folder="../static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/list/")
def getCrimeList():
    # need to complete list, possibly add values?
    list = [
    {"text": "Solicitation for murder (RS 14:28.1)"},
    {"text": "First degree murder (RS 14:30)"},
    {"text": "Solicitation for murder (RS 14:28.1)"},
    {"text": "Second degree murder (RS 14:30.1)"},
    {"text": "Manslaughter (RS 14:31)"},
    {"text": "Aggravated battery (RS 14:34)"}
    ]
    return jsonify(results = list)



if __name__ == "__main__":
    app.run(debug=True)
