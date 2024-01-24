from famousFormations import createFormations
import random
from datetime import date, timedelta

nums = 10
randomNumbers = [random.randint(0,len(createFormations())-1) for _ in range(10)]
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