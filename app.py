from famousFormations import createFormations


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
    print(formation.formation)
    return {"team":formation.team,"date":formation.date,"lineup":formation.lineup,"bench":formation.bench, "manager":formation.manager,"formation":formation.formation}

if __name__ == "__main__":
    app.run(debug=True,port=5002)
