import datetime
from datetime import timedelta
import sys


crimetypes = ['violentcrime', 'sexualcrime', 'violsexcrime', 'othercrime']
sentenceyears = 0
sentencemonths = 0

##def getdate():
##    date1 = input(datetime.date)
##    return date1

##Card 1
Q1 = "Welcome. \n This application is designed to calculate release dates" \
"of individuals sentenced under Louisiana law. \n The application first" \
" determines whether an individual is eligible for early release based on" \
" good time and/or parole. It then calculates individuals’ good time" \
" release dates, parole eligibility dates, and the last possible day" \
" they can be released. \n The release date calculation process only covers" \
" cases with an offense date that is later than November 1, 2017."

##Card 2
Q2 = "Disclaimer \n Important: Please note that this application does not" \
" provide legal services or legal advice. Your use of this application does" \
" not form an attorney-client relationship with any party."

##Card 3
Q3 = "Next, please tell us about the crime your client is charged with:"
Q4 = "Will the individual be sentenced under the habitual offender statute?"
Q5 = "What sentence will your client be given? Please enter the length" \
" of the sentence in years and/or months:"

##Card 4
Q6 = "Has your client been convicted before of other felonies?"
Q7 = "How many prior felony convictions does your client have?"

##Card 5
Q8 = "For each of your client's prior convictions, select the crime, below:"

##Card 6
Q9 = "When was your client arrested?"
Q10 = "When will your client be convicted?"

print(Q1)
input("Press Enter to continue...")
print(Q2)
input("Press Enter to continue...")
print(Q3)
currcharge = input("Enter the name of the crime from the following list." \
" If your client is charged with a crime that is not listed, please enter" \
" the option A crime not included in this list\n" \
"\t Solicitation for murder (RS 14:28.1) \n"
"\t First degree murder (RS 14:30) \n"
"\t Second degree murder (RS 14:30.1) \n"
"\t Manslaughter (RS 14:31) \n"
"\t Second degree battery (RS 14:34.1) \n"
"\t Aggravated assault (RS 14:37) \n"
"\t Vehicular homicide with blood alcohol concentration over 0.20 percent (RS 14:32.1) \n"
"\t Aggravated assault upon a dating partner (RS 14:34.9.1)\n"
"\t Aggravated second degree battery (RS 14:34.7)\n"
"\t Domestic abuse aggravated assault (RS 14:37.7)\n"
"\t Aggravated assault upon a peace officer (RS 14:37.2)\n"
"\t Aggravated assault with a firearm (RS 14:37.4)\n"
"\t Aggravated kidnapping (RS 14:44)\n"
"\t Second degree kidnapping (RS 14:44.1)\n"
"\t Simple kidnapping (RS 14:45)\n"
"\t Aggravated arson (RS 14:51)\n"
"\t Aggravated criminal damage to property (RS 14:55)\n"
"\t Aggravated burglary (RS 14:60)\n"
"\t Armed robbery (RS 14:64)\n"
"\t First degree robbery (RS 14:64.1)\n"
"\t Carjacking (RS 14:64.2)\n"
"\t Second degree robbery (RS 14:64.4)\n"
"\t Armed robbery or attempted armed robbery with use of firearm (RS 14:64.3)\n"
"\t Simple robbery (RS 14:65)\n"
"\t Purse snatching (RS 14:65.1)\n"
"\t Assault by drive-by shooting (RS 14:37.1)\n"
"\t Terrorism (RS 14:128.1)\n"
"\t Disarming of a peace officer (RS 14:34.6)\n"
"\t Stalking (RS 14:40.2)\n"
"\t Second degree cruelty to juveniles (RS 14:93.2.3)\n"
"\t Aggravated flight from an officer (RS 14:108.1)\n"
"\t Battery of a police officer (RS 14:34.2)\n"
"\t Home invasion (RS 14:62.8)\n"
"\t Crime against nature (RS 14:89)\n"
"\t Crime against nature by solicitation (RS 14:89.2B3)\n"
"\t Felony carnal knowledge of a juvenile (RS 14:80)\n"
"\t Indecent behavior with juveniles (RS 14:81)\n"
"\t Pornography involving juveniles (RS 14:81.1)\n"
"\t Molestation of a juvenile or a person with a physical or mental disability (RS 14:81.2)\n"
"\t Computer-aided solicitation of a minor (RS 14:81.3)\n"
"\t Prohibited sexual conduct between an educator and student (RS 14:81.4)\n"
"\t Prostitution: persons under eighteen (RS 14:82.1)\n"
"\t Purchase of commercial sexual activity (RS 14:82.2C4)\n"
"\t Contributing to the delinquency of juveniles (RS 14:92A7)\n"
"\t Sexual battery of persons with infirmities (RS 14:93.5)\n"
"\t Obscenity by solicitation of a person under the age of seventeen (RS 14:106A5)\n"
"\t Video voyeurism (RS 14:283)\n"
"\t Rape (RS 14:41)\n"
"\t Oral sexual battery (RS 14:43.3)\n"
"\t Voyeurism: second conviction (RS 14:283.1)\n"
"\t Sexual battery (RS 14:43.1)\n"
"\t Second degree sexual battery (RS 14:43.2)\n"
"\t Aggravated or first degree rape (RS 14:42)\n"
"\t Forcible or second degree rape (RS 14:42.1)\n"
"\t Simple or third degree rape (RS 14:43)\n"
"\t Intentional exposure to AIDS virus (RS 14:43.5)\n"
"\t Aggravated crime against nature (RS 14:89.1)\n"
"\t Trafficking of children for sexual purposes (RS 14:46.3)\n"
"\t Human trafficking (RS 14:46.2B2)\n"
"\t A crime not included in this list\n"
"Current charge: ")

ishabitualoffenderstr = input(Q4 + "")
if ishabitualoffenderstr == 'yes' or ishabitualoffenderstr == 'Yes' or ishabitualoffenderstr == 'y':
    ishabitualoffender = True
else:
    ishabitualoffender = False

print(Q5)
sentenceyears = int(input("Years: "))
sentencemonths = int(input("Months: "))
totalsentence = (sentencemonths + (sentenceyears*12))*30

haspriorsstr = input(Q6)
if haspriorsstr == 'yes' or haspriorsstr == 'Yes' or haspriorsstr == 'y':
    haspriors = True
else:
    haspriors = False

if haspriors == False:
    numpriors = 0
if haspriors == True:
    numpriors = input(Q7)
    priorcharges = []
    print(Q8)
    print("Enter the names of prior convictions from the following list." \
    " If your client is charged with a crime that is not listed, please enter" \
    " the option A crime not included in this list\n" \
    "\t Solicitation for murder (RS 14:28.1) \n"
    "\t First degree murder (RS 14:30) \n"
    "\t Second degree murder (RS 14:30.1) \n"
    "\t Manslaughter (RS 14:31) \n"
    "\t Second degree battery (RS 14:34.1) \n"
    "\t Aggravated assault (RS 14:37) \n"
    "\t Vehicular homicide with blood alcohol concentration over 0.20 percent (RS 14:32.1) \n"
    "\t Aggravated assault upon a dating partner (RS 14:34.9.1)\n"
    "\t Aggravated second degree battery (RS 14:34.7)\n"
    "\t Domestic abuse aggravated assault (RS 14:37.7)\n"
    "\t Aggravated assault upon a peace officer (RS 14:37.2)\n"
    "\t Aggravated assault with a firearm (RS 14:37.4)\n"
    "\t Aggravated kidnapping (RS 14:44)\n"
    "\t Second degree kidnapping (RS 14:44.1)\n"
    "\t Simple kidnapping (RS 14:45)\n"
    "\t Aggravated arson (RS 14:51)\n"
    "\t Aggravated criminal damage to property (RS 14:55)\n"
    "\t Aggravated burglary (RS 14:60)\n"
    "\t Armed robbery (RS 14:64)\n"
    "\t First degree robbery (RS 14:64.1)\n"
    "\t Carjacking (RS 14:64.2)\n"
    "\t Second degree robbery (RS 14:64.4)\n"
    "\t Armed robbery or attempted armed robbery with use of firearm (RS 14:64.3)\n"
    "\t Simple robbery (RS 14:65)\n"
    "\t Purse snatching (RS 14:65.1)\n"
    "\t Assault by drive-by shooting (RS 14:37.1)\n"
    "\t Terrorism (RS 14:128.1)\n"
    "\t Disarming of a peace officer (RS 14:34.6)\n"
    "\t Stalking (RS 14:40.2)\n"
    "\t Second degree cruelty to juveniles (RS 14:93.2.3)\n"
    "\t Aggravated flight from an officer (RS 14:108.1)\n"
    "\t Battery of a police officer (RS 14:34.2)\n"
    "\t Home invasion (RS 14:62.8)\n"
    "\t Crime against nature (RS 14:89)\n"
    "\t Crime against nature by solicitation (RS 14:89.2B3)\n"
    "\t Felony carnal knowledge of a juvenile (RS 14:80)\n"
    "\t Indecent behavior with juveniles (RS 14:81)\n"
    "\t Pornography involving juveniles (RS 14:81.1)\n"
    "\t Molestation of a juvenile or a person with a physical or mental disability (RS 14:81.2)\n"
    "\t Computer-aided solicitation of a minor (RS 14:81.3)\n"
    "\t Prohibited sexual conduct between an educator and student (RS 14:81.4)\n"
    "\t Prostitution: persons under eighteen (RS 14:82.1)\n"
    "\t Purchase of commercial sexual activity (RS 14:82.2C4)\n"
    "\t Contributing to the delinquency of juveniles (RS 14:92A7)\n"
    "\t Sexual battery of persons with infirmities (RS 14:93.5)\n"
    "\t Obscenity by solicitation of a person under the age of seventeen (RS 14:106A5)\n"
    "\t Video voyeurism (RS 14:283)\n"
    "\t Rape (RS 14:41)\n"
    "\t Oral sexual battery (RS 14:43.3)\n"
    "\t Voyeurism: second conviction (RS 14:283.1)\n"
    "\t Sexual battery (RS 14:43.1)\n"
    "\t Second degree sexual battery (RS 14:43.2)\n"
    "\t Aggravated or first degree rape (RS 14:42)\n"
    "\t Forcible or second degree rape (RS 14:42.1)\n"
    "\t Simple or third degree rape (RS 14:43)\n"
    "\t Intentional exposure to AIDS virus (RS 14:43.5)\n"
    "\t Aggravated crime against nature (RS 14:89.1)\n"
    "\t Trafficking of children for sexual purposes (RS 14:46.3)\n"
    "\t Human trafficking (RS 14:46.2B2)\n"
    "\t A crime not included in this list\n")
    for i in range(numpriors):
        if i == 1:
            priorconvic = input("Enter prior conviction: ")
        else:
            priorconvic = input("Enter additional prior conviction: ")
        priorcharges = priorcharges.append(priorconvic)

##def getdate():
##    isValid=False
##    while not isValid:
        ##userIn = input("Type Date dd/mm/yy: ")
##        try:
##            userIn = input("Type Date dd/mm/yy: ")
    ##        d = datetime.datetime.strptime(userIn, "%d/%m/%y")
##            isValid=True
##        except:
##            print("Not a valid date. Try again.\n")
##        return d

print(Q9)
arrestdate = datetime.datetime.strptime(input("Type Date dd/mm/yy: "), "%d/%m/%y")
print(Q10)
convictdate = datetime.datetime.strptime(input("Type Date dd/mm/yy: "), "%d/%m/%y")

##Conviction classification
violentcharges = ["Solicitation for murder (RS 14:28.1)",
"First degree murder (RS 14:30)",
"Second degree murder (RS 14:30.1)",
"Manslaughter (RS 14:31)",
"Second degree battery (RS 14:34.1)",
"Aggravated assault (RS 14:37)",
"Vehicular homicide with blood alcohol concentration over 0.20 percent (RS 14:32.1)",
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
"Home invasion (RS 14:62.8)"]
sexualcharges = ["Crime against nature (RS 14:89)",
"Crime against nature by solicitation (RS 14:89.2B3)"
"Felony carnal knowledge of a juvenile (RS 14:80)"
"Indecent behavior with juveniles (RS 14:81)"
"Pornography involving juveniles (RS 14:81.1)"
"Molestation of a juvenile or a person with a physical or mental disability (RS 14:81.2)"
"Computer-aided solicitation of a minor (RS 14:81.3)"
"Prohibited sexual conduct between an educator and student (RS 14:81.4)"
"Prostitution: persons under eighteen (RS 14:82.1)"
"Purchase of commercial sexual activity (RS 14:82.2C4)"
"Contributing to the delinquency of juveniles (RS 14:92A7)"
"Sexual battery of persons with infirmities (RS 14:93.5)"
"Obscenity by solicitation of a person under the age of seventeen (RS 14:106A5)"
"Video voyeurism (RS 14:283)"
"Rape (RS 14:41)"
"Oral sexual battery (RS 14:43.3)"
"Voyeurism: second conviction (RS 14:283.1)"]
violsexcharges = ["Sexual battery (RS 14:43.1)"
"Second degree sexual battery (RS 14:43.2)"
"Aggravated or first degree rape (RS 14:42)"
"Forcible or second degree rape (RS 14:42.1)"
"Simple or third degree rape (RS 14:43)"
"Intentional exposure to AIDS virus (RS 14:43.5)"
"Aggravated crime against nature (RS 14:89.1)"
"Trafficking of children for sexual purposes (RS 14:46.3)"
"Human trafficking (RS 14:46.2B2)"]
othercharges = ["A crime not included in this list"]
if currcharge in violentcharges:
    currchargetype = "violentcrime"
elif currcharge in sexualcharges:
    currchargetype = "sexualcrime"
elif currcharge in violsexcharges:
    currchargetype = "violsexcrime"
else:
    currchargetype = "othercrime"

##Prior charges classification
violpriors = 0
sexpriors = 0
violsexpriors = 0
otherpriors = 0
if haspriors == True:
    for charge in priorcharges:
        if charge in violentcharges:
            violpriors = violpriors + 1
        elif charge in sexualcharges:
            sexpriors = sexpriors + 1
        elif charge in violsexcharges:
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
elif currchagetype == "violsexcrime":
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
pretrialdetention = abs((convictdate - arrestdate))
sentencedeltadays = timedelta(days = totalsentence)
if eligibleparole == True:
    parolereleasedate = convictdate + (sentencedeltadays * parolemultiplier)
    paroledatestring= (str(parolereleasedate)[:10])
    print("Your client is eligible for parole after having served " +
    str(int(parolemultiplier*100)) + "%" + " of their sentence. " +
    "Your client will be eligible for parole on " + paroledatestring)
else:
    "Your client is not eligible for parole."

#Good time eligibility and calculations
if currchargetype == "othercrime":
    if numpriors == 0:
        eligibleGT = True
        GTmultiplier = 0.35
    else:
        if ishabitualoffender == True:
            eligibleGT = False
        else:
            eligibleGT = True
            GTmultiplier = 0.35
elif currchargetype == "violentcrime":
    if numpriors == 0:
        eligibleGT = True
        GTmultiplier = 0.75
    else:
        if ishabitualoffender == True:
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
    GTreleasedate = convictdate + (sentencedeltadays * GTmultiplier)
    GTdatestring= (str(GTreleasedate)[:10])
    print("Your client is eligible for good time release after having served " +
    str(int(GTmultiplier*100)) + "%" + " of their sentence. " +
    "Your client will be eligible for good time release on " + GTdatestring)
else:
    "Your client is not eligible for good time release."

##Last possible release date
lastreleasedate = convictdate + sentencedeltadays
lastdatestring= (str(lastreleasedate)[:10])
print("Last possible release date: Your client will be eligible" +
" for good time release on " + lastdatestring)
