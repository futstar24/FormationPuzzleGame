from famousFormations import createFormations
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import random


randomNum = None

scheduler = BackgroundScheduler()

def getRandomNum():
    global randomNum
    print("running")
    randomNum = random.randint(1,10)

scheduler.add_job(getRandomNum, 'interval', seconds=5)
scheduler.start()

formations = createFormations()

from flask import *

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("dailyPage.html")

@app.route("/dailyFormation", methods = ["GET"])
def dailyFormation():
    formation = formations[0]
    print(randomNum)
    return {"team":formation.team,"date":formation.date,"lineup":formation.lineup,"bench":formation.bench, "manager":formation.manager,"formation":formation.formation,"randomNumber":randomNum}

if __name__ == "__main__":
    app.run(debug=True,port=5002,use_reloader=False)
