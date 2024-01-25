from famousFormations import createFormations, createTeams
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

players = []
with open("players.txt","r",encoding="utf-8") as input:
    lines = input.readlines()
    for line in lines:
        players.append(line.split("\n")[0])

def nextDay():
    global randomNum
    today = date.today()
    randomNum = datesAndNums[str(today)]

formations = createFormations()
teams = createTeams(formations)

from flask import *

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/daily")
def home():
    return render_template("dailyPage.html")

@app.route("/dailyFormation", methods = ["GET"])
def dailyFormation():
    formation = formations[randomNum]
    return {"team":formation.team,"opposition":formation.opposition,"tie":formation.tie,"date":formation.date,"lineup":formation.lineup,"bench":formation.bench, "manager":formation.manager,"formation":formation.formation,"randomNumber":randomNum}

@app.route("/teamSelector", methods = ["GET"])
def teamSelector():
    return render_template("teamSelector.html")

currentTeam = None
@app.route("/teamSelector/<teamName>", methods = ["GET"])
def teamSelectorWithName(teamName):
    global currentTeam
    print("name",teamName)
    currentTeam = teamName
    return render_template("gameSelector.html",team = teamName)

currentGameId = None
@app.route("/teamSelector/<teamName>/<gameId>", methods = ["GET"])
def teamSelectorWithNameAndGame(teamName,gameId):
    global currentGameId
    teamFormations = teams[teamName]
    for formation in teamFormations:
        if gameId in formation.id:
            currentGameId = gameId
            return render_template("teamLevelPage.html")

@app.route("/sendTeams", methods = ["GET"])
def sendTeams():
    sendTeams = list(teams.keys())
    return {"teams":sendTeams}

@app.route("/sendGames/<teamName>", methods = ["GET"])
def sendGames(teamName):
    teamFormations = teams[teamName]
    result = []
    for formation in teamFormations:
        result.append([formation.team,formation.opposition,formation.tie,formation.date,formation.lineup,formation.bench,formation.manager,formation.formation,formation.id])
    return {"result":result}

@app.route("/sendGameInfo", methods = ["GET"])
def sendGameId():
    print("here")
    teamFormations = teams[currentTeam]
    for formation in teamFormations:
        print("looping")
        if currentGameId in formation.id:
            print("returning")
            return {"team":formation.team,"opposition":formation.opposition,"tie":formation.tie,"date":formation.date,"lineup":formation.lineup,"bench":formation.bench, "manager":formation.manager,"formation":formation.formation}

@app.route("/sendPlayers", methods = ["GET"])
def sendPlayers():
    return players

scheduler = BackgroundScheduler()
nextDay()
scheduler.add_job(nextDay, trigger=CronTrigger(hour=0,minute=0,second=0))
scheduler.start()

if __name__ == "__main__":
    app.run(debug=True,port=5002,use_reloader=False)

