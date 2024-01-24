def createFormations():
    formations = [
        Formation("Manchester City",[5,13,2012],["Sergio Aguero","David Silva","Carlos Tevez","Samir Nasri","Yaya Toure","Gareth Barry","Gael Clichy","Joleon Lescott","Vincent Kompany","Paulo Zabaleta","Joe Hart"],["Costel Pantilimon","Aleksander Kolarov","Micah Richards","Nigel de Jong","James Milner","Mario Balotelli","Edin Dzeko"],"Roberto Mancini",[4,2,3,1]),






    ]
    return formations
    

class Formation:
    def __init__(self,team,date,lineup,bench,manager,formation):
        self.team = team
        self.date = date
        self.lineup = lineup
        self.formation = formation
        self.bench = bench
        self.manager = manager