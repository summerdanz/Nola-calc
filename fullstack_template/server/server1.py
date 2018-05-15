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
    global list1

    list1 = [
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
    return jsonify(results = list1)

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
     global convicted_before
     global conviction_count
     convicted_before = json['convictedBefore']
     conviction_count = json['convictionCount']
     #return jsonify(convicted_before=convicted_before, conviction_count=conviction_count)
     return jsonify('OK')

@app.route('/currentcharge',  methods=['POST'])
def post_crime_info():
     json = request.get_json()
     global crime_selected
     global habitual_offender
     global sentence_year
     global sentence_month
     crime_selected = json['crimeSelected']
     habitual_offender = json['isHabitualOffender']
     sentence_year = json['sentenceYear']
     sentence_month = json['sentenceMonth']
     return jsonify('OK')

@app.route('/selectFelonies',  methods=['POST'])
def post_select_felonies():
     json = request.get_json()
     global previousFeloniesValue
     previousFeloniesValue = json['whichFelonies']
     # this will give you an array of values [0,1,2 etc] that correspond
     # to the index of the crime selected from the list
     # ie solicitation for murder =0; Second degree battery (RS 14:34.1) =4, etc;
     # return jsonify(relation=relation) --- this is how you would return dataType
     return jsonify('OK')

@app.route('/dates',  methods=['POST'])
def post_dates():
     json = request.get_json()
     global arrest_date
     global release_value
     global release_date
     global conviction_date
     arrest_date = json['arrestDate']
     release_value = json['releaseValue']
     release_date = json['releaseDate']
     conviction_date = json['convictDate']
     return jsonify('OK')

#running functions
getCrimeList()
post_prev_felonies()
post_crime_info()
post_select_felonies()
post_dates()

totalsentence = (sentence_month + (sentence_year*12))*30

#Current charge classification
if crime_selected[0] in range(0, 32):
    currchargetype = "violentcrime"
elif crime_selected[0] in range(33, 49):
    currchargetype = "sexualcrime"
elif crime_selected[0] in range(50, 58):
    currchargetype = "violsexcrime"
else:
    currchargetype = "othercrime"

#Prior charge classification
violpriors = 0
sexpriors = 0
violsexpriors = 0
otherpriors = 0
if convicted_before == True:
    for charge in previousFeloniesValue:
        if charge in range(0, 32):
            violpriors = violpriors + 1
        elif charge in range(33, 49):
            sexpriors = sexpriors + 1
        elif charge in range(50, 58):
            violsexpriors = violsexpriors + 1
        else:
            otherpriors = otherpriors + 1

#Parole release eligibility and calculations
if currchargetype == "othercrime":
    eligibleparole = True
    parolemultiplier = 0.25
elif currchargetype == "violentcrime":
    if numpriors == 0:
        eligibleparole = True
        parolemultiplier = 0.35
    elif (violpriors + violsexpriors) == 0:
        eligibleparole = True
        parolemultiplier = 0.65
    elif (violpriors + violsexpriors) == 1:
        eligibleparole = True
        parolemultiplier = 0.75
    else:
        eligibleparole = False
elif currchargetype == "sexualcrime":
    if numpriors == 0:
        eligibleparole = True
        parolemultiplier = 0.75
    elif (sexpriors + violsexpriors) == 0:
        eligibleparole = True
        parolemultiplier = 0.75
    elif (sexpriors + violsexpriors) == 1:
        eligibleparole = True
        parolemultiplier = 0.75
    else:
        eligibleparole = False
elif currchargetype == "violsexcrime":
    if numpriors == 0:
        eligibleparole = True
        parolemultiplier = 0.75
    elif (sexpriors + violpriors + violsexpriors) == 0:
        eligibleparole = True
        parolemultiplier = 0.75
    elif (sexpriors + violpriors + violsexpriors) == 1:
        eligibleparole = True
        parolemultiplier = 0.75
    else:
        eligibleparole = False

pretrialdetention = abs((conviction_date - arrest_date))
sentencedeltadays = timedelta(days = totalsentence)
if eligibleparole == True:
    parolereleasedate = conviction_date + (sentencedeltadays * parolemultiplier)
    paroledatestring= (str(parolereleasedate)[:10])
    paroleEligibilityString = "Your client is eligible for parole after having served " +
    str(int(parolemultiplier*100)) + "%" + " of their sentence. "
else:
    paroleEligibilityString = "Your client is not eligible for parole."

if convicted_before == False:
    numpriors = 0
if convicted_before == True:
    numpriors = conviction_count

#Good time eligibility and calculations
if currchargetype == "othercrime":
    if numpriors == 0:
        eligibleGT = True
        GTmultiplier = 0.35
    else:
        if habitual_offender == True:
            eligibleGT = False
        else:
            eligibleGT = True
            GTmultiplier = 0.35
elif currchargetype == "violentcrime":
    if numpriors == 0:
        eligibleGT = True
        GTmultiplier = 0.75
    else:
        if habitual_offender == True:
            eligibleGT = False
        else:
            if (sexpriors + violpriors + violsexpriors) > 0:
                eligibleGT = False
            else:
                eligibleGT = True
                GTmultiplier = 0.75
elif currchargetype == "sexualcrime" or currchargetype == "violsexcrime":
    eligibleGT = False
if eligibleGT == True:
    GTreleasedate = conviction_date + (sentencedeltadays * GTmultiplier)
    GTdatestring= (str(GTreleasedate)[:10])
    earlyReleaseString = "Your client is eligible for good time release after having served " +
    str(int(GTmultiplier*100)) + "%" + " of their sentence. "
else:
    earlyReleaseString = "Your client is not eligible for good time release."

##Last possible release date
lastreleasedate = conviction_date + sentencedeltadays
lastdatestring= (str(lastreleasedate)[:10])



@app.route("/results")
def getResults():
    # Below are examples of how the data should be stored - this is where the calculations will be sent to the results page
    goodTimeReleaseDate = GTdatestring
    earlyRelease = earlyReleaseString
    paroleEligibilityDate = paroledatestring
    paroleEligibility = paroleEligibilityString
    lastReleaseDate = lastdatestring
    return jsonify(goodTimeReleaseDate=goodTimeReleaseDate, earlyRelease=earlyRelease, paroleEligibility=paroleEligibility, paroleEligibilityDate=paroleEligibilityDate, lastReleaseDate=lastReleaseDate)

if __name__ == "__main__":
    app.run(debug=True)
