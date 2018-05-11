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
     "Solicitation for murder (RS 14:28.1) ",
    "First degree murder (RS 14:30) ",
    "Second degree murder (RS 14:30.1) ",
    "Manslaughter (RS 14:31) ",
    "Second degree battery (RS 14:34.1) ",
    "Aggravated assault (RS 14:37) ",
    "Vehicular homicide with blood alcohol concentration over 0.20 percent (RS 14:32.1) ",
    "Aggravated assault upon a dating partner (RS 14:34.9.1)",
    "Aggravated second degree battery (RS 14:34.7)",
    "Domestic abuse aggravated assault (RS 14:37.7)",
    "Aggravated assault upon a peace officer (RS 14:37.2)",
    "Aggravated assault with a firearm (RS 14:37.4)",
    "Aggravated kidnapping (RS 14:44)",
    "Second degree kidnapping (RS 14:44.1)",
    "Simple kidnapping (RS 14:45)",
    "Aggravated arson (RS 14:51)",
    "Aggravated criminal damage to property (RS 14:55)",
    "Aggravated burglary (RS 14:60)",
    "Armed robbery (RS 14:64)",
    "First degree robbery (RS 14:64.1)",
    "Carjacking (RS 14:64.2)",
    "Second degree robbery (RS 14:64.4)",
    "Armed robbery or attempted armed robbery with use of firearm (RS 14:64.3)",
    "Simple robbery (RS 14:65)",
    "Purse snatching (RS 14:65.1)",
    "Assault by drive-by shooting (RS 14:37.1)",
    "Terrorism (RS 14:128.1)",
    "Disarming of a peace officer (RS 14:34.6)",
    "Stalking (RS 14:40.2)",
    "Second degree cruelty to juveniles (RS 14:93.2.3)",
    "Aggravated flight from an officer (RS 14:108.1)",
    "Battery of a police officer (RS 14:34.2)",
    "Home invasion (RS 14:62.8)",
    "Crime against nature (RS 14:89)",
    "Crime against nature by solicitation (RS 14:89.2B3)",
    "Felony carnal knowledge of a juvenile (RS 14:80)",
    "Indecent behavior with juveniles (RS 14:81)",
    "Pornography involving juveniles (RS 14:81.1)",
    "Molestation of a juvenile or a person with a physical or mental disability (RS 14:81.2)",
    "Computer-aided solicitation of a minor (RS 14:81.3)",
    "Prohibited sexual conduct between an educator and student (RS 14:81.4)",
    "Prostitution: persons under eighteen (RS 14:82.1)",
    "Purchase of commercial sexual activity (RS 14:82.2C4)",
    "Contributing to the delinquency of juveniles (RS 14:92A7)",
    "Sexual battery of persons with infirmities (RS 14:93.5)",
    "Obscenity by solicitation of a person under the age of seventeen (RS 14:106A5)",
    "Video voyeurism (RS 14:283)",
    "Rape (RS 14:41)",
    "Oral sexual battery (RS 14:43.3)",
    "Voyeurism: second conviction (RS 14:283.1)",
    "Sexual battery (RS 14:43.1)",
    "Second degree sexual battery (RS 14:43.2)",
    "Aggravated or first degree rape (RS 14:42)",
    "Forcible or second degree rape (RS 14:42.1)",
    "Simple or third degree rape (RS 14:43)",
    "Intentional exposure to AIDS virus (RS 14:43.5)",
    "Aggravated crime against nature (RS 14:89.1)",
    "Trafficking of children for sexual purposes (RS 14:46.3)",
    "Human trafficking (RS 14:46.2B2)",
    "A crime not included in this list"
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
