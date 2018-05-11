from flask import Flask, render_template, request
from flask import jsonify
from json import *
from flask_cors import CORS

app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/list/")
def getCrimeList():
    # need to complete list, possibly add values?
    list = [
     "Solicitation for murder (RS 14:28.1)",
     "First degree murder (RS 14:30)",
     "Solicitation for murder (RS 14:28.1)",
     "Second degree murder (RS 14:30.1)",
     "Manslaughter (RS 14:31)",
    "Aggravated battery (RS 14:34)"
    ]
    return jsonify(results = list)

@app.route('/disclaimer',  methods=['POST'])
def post_disclaimer():
     json = request.get_json()
     disclaimer_checked = json['isDisclaimerChecked']
     return jsonify('OK')

@app.route('/relation',  methods=['POST'])
def post_relation():
     json = request.get_json()
     relation = json['relation']
     # return jsonify(relation=relation) --- this is how you would return dataType
     return jsonify('OK')

@app.route('/PreviousFelonies',  methods=['POST'])
def post_prev_felonies():
     json = request.get_json()
     convicted_before = json['convictedBefore']
     conviction_count = json['convictionCount']
     #return jsonify(convicted_before=convicted_before, conviction_count=conviction_count)
     return jsonify('OK')

@app.route('/currentcharge',  methods=['POST'])
def post_crime_info():
     json = request.get_json()
     crime_selected = json['crimeSelected']
     habitual_offender = json['isHabitualOffender']
     sentence_year = json['sentenceYear']
     sentence_month = json['sentenceMonth']
     return jsonify('OK')


if __name__ == "__main__":
    app.run(debug=True)
