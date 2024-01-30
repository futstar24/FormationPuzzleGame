class Formation:
    def __init__(self,team,opposition,score,tie,date,lineup,bench,manager,formation,id):
        self.team = team
        self.date = date
        self.opposition = opposition
        self.score = score
        self.tie = tie
        self.lineup = lineup
        self.formation = formation
        self.bench = bench
        self.manager = manager
        self.id = id

def createFormations():
    uuids = []
    with open("ids.txt","r",encoding="utf-8") as input:
        lines = input.readlines()
        for line in lines:
            uuids.append(line)

    formations = [
        Formation("Manchester City","Queens Park Rangers",[3,2],"Balotelli... AGUERRRROOOOO!!!",[5,13,2012],["Sergio Aguero","David Silva","Carlos Tevez","Samir Nasri","Yaya Toure","Gareth Barry","Gael Clichy","Joleon Lescott","Vincent Kompany","Paulo Zabaleta","Joe Hart"],["Costel Pantilimon","Aleksander Kolarov","Micah Richards","Nigel de Jong","James Milner","Mario Balotelli","Edin Dzeko"],"Roberto Mancini",[4,2,3,1],""),
        Formation("Manchester City","Inter Milan",[2,1],"The Champions!!!!",[6,10,2023],["Erling Haaland","Kevin De Bruyne","Ilkay Gundogan","Jack Grealish","Rodri","John Stones","Bernardo Silva","Ruben Dias","Nathan Ake","Manuel Akanji","Ederson"],["Scott Carson","Stefan Ortega","Aymeric Laporte","Sergio Gomez","Rico Lewis","Kyle Walker","Maximo Perrone","Kalvin Phillips","Cole Palmer","Phil Foden","Riyad Mahrez","Julian Alvarez"],"Pep Guardiola",[3,4,2,1],""),






    ]

    for i in range(len(formations)):
        formations[i].id = uuids[i]
    return formations
    
def createTeams(formations):
    teams = {}
    for formation in formations:
        if formation.team in teams:
            teams[formation.team].append(formation)
        else:
            teams[formation.team] = [formation]
    return teams

def createPlayers(formations):
    players = []
    for formation in formations:
        for player in formation.lineup:
            if player not in players:
                players.append(player)
        for player in formation.bench:
            if player not in players:
                players.append(player)
    return players


def waltersList():

    #teamName, opponentName, score (as list [teamName, opponentName]), gameTitle, gameDate (list of day month year), lineup, bench, manager, formation (as list), empty quotes
    formations = [Formation()

    ]

def nicksList():

    #teamName, opponentName, score (as list [teamName, opponentName]), gameTitle, gameDate (list of day month year), lineup, bench, manager, formation (as list), empty quotes
    formations = [Formation()

    ]

def jaspersList():

    #teamName, opponentName, score (as list [teamName, opponentName]), gameTitle, gameDate (list of day month year), lineup, bench, manager, formation (as list), empty quotes
    formations = [Formation()

    ]