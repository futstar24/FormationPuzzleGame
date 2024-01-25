from famousFormations import createFormations,createPlayers
import random
from datetime import date, timedelta
import uuid

nums = 10
formations = createFormations()
players = createPlayers(formations)
randomNumbers = [random.randint(0,len(formations)-1) for _ in range(10)]
today = date.today()
with open("randomNumbers.txt", 'w', encoding="utf-8") as output:
        i = 0
        for randomNumber in randomNumbers:
            i += 1
            if i == 1000:
                output.write(f'{today} {randomNumber}')
            else:
                 output.write(f'{today} {randomNumber}\n')
            today += timedelta(days=1)

with open("ids.txt","w",encoding="utf-8") as output:
     for i in range(len(formations)):
          output.write(f'{uuid.uuid4()}\n')

with open("players.txt","w",encoding="utf-8") as output:
     for player in players:
          output.write(f'{player}\n')