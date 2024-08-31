# guess_num.py
# Danny Yu

# Number guessing game

#think of a number from 1 to 3
import random
pick = random.randint(1,3)

# User's guess

guess = int(input("Enter 1, 2, or 3"))

# Determine if the guess is too high , low, or correct
if guess == pick:
    print("Correct")
elif guess > pick:
    print("Too high")
else:
    print("Too low")

print("I was thinking of", str(pick) + ".")
