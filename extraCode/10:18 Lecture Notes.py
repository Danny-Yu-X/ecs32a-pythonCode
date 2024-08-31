# x += 1

""""n = 3
while n > 0:
    print(n)
    n = n-1
print("Contact")"""
#______________________
""""x = input("Enter an integer between 0 and 10:")
x = int(x)
i = 0
while i <= 10:
    i = i + 1
    print(x, "*", i, "=", x*i)"""

#___________________________________
"""x = input("Enter an integer between 0 and 10:")
x = int(x)
i = 0
while True:
    print(x, "*", i, "=", x*i)
    if i ==12:
        break
    i = i + 1
print("Done")"""

#________________________________
while True:
    ans = input(">")
    if ans == "exit":
        break
    if ans == "pause":
        continue
    print(ans)
#________________________
"""import random
wins = 0
games = 0
while True:
    pick = random.randint(1,3)
    guess = (input("Guess a number (1-3) or q to quit:"))
    games = games + 1
    if  guess == "q":
        break
    if pick == guess:
        print("Correct")
        wins = wins + 1
    else:
        print("Incorrect")
    ans = input("Play again?")
    
print("You won", wins, "out of", games, "games.")"""
#__________________________________

