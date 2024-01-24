from famousFormations import createFormations
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import random
from datetime import date, timedelta

randomNum = None
datesAndNums = {}

with open("randomNumbers.txt","r",encoding="utf-8") as input:
    lines = input.readlines()
    for line in lines:
        dateNum = line.split("\n")[0]
        day = dateNum.split(" ")[0]
        num = int(dateNum.split(" ")[1])
        datesAndNums[day] = num

def nextDay():
    global randomNum
    today = date.today()
    randomNum = datesAndNums[str(today)]

formations = createFormations()

from flask import *

app = Flask(__name__)

@app.route("/", methods = ["GET"])
@app.route("/home", methods = ["GET"])
def home():
    return render_template("dailyPage.html")

@app.route("/dailyFormation", methods = ["GET"])
def dailyFormation():
    formation = formations[randomNum]
    return {"team":formation.team,"date":formation.date,"lineup":formation.lineup,"bench":formation.bench, "manager":formation.manager,"formation":formation.formation,"randomNumber":randomNum}

scheduler = BackgroundScheduler()
nextDay()
scheduler.add_job(nextDay, trigger=CronTrigger(hour=0,minute=0,second=0))
scheduler.start()

if __name__ == "__main__":
    app.run(debug=True,port=5002,use_reloader=False)

