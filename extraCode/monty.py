#Monty Hall Problem

import = random

games = 1000000
stick _wins = 0
change_wins = 0
doors = ["A,", "B", "C"]

for i in range(games):

    prize = random.choice(doors)

    pick = random.choice(doors)


    #Monty comes in and opens a door
    #Two doors left: one with the prize, one without

    #scenario 1: don't change mind wins

    if pick == prize:
        #print("You win - by sticking")
        stick_wins = stick_wins + 1
    #scenario 2: did change mind
    if pick != prize:
        #print("You win - by changing")
        change_wins = change_wins + 1


print("Stick_wins", stick_wins, "out of", games, "games", stick_wins/games)
print("Change wins", change_wins, "out of", games, "games", change_wins/games)
    

