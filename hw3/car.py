# car.py
# Danny Yu
# This program prompts the user to guess the price of a car.
# If their price is too high, they receive the output of their price beiing too high.
# If their price is too low, they receive the output of their price being too low.
# Once they guess correctly, the program outputs their number of guesses and if they exceeded 5 guesses they would receive the output that tell them they had too many guesses.

# price in dollars
price = 44500 # set price for the car


print("Guess the price and win the prize!")

rounds = 1 # keeps track of the number of guesses
# loops until the user inputs a guess that matches the price of the car
# iterating over rounds
while True:
    guess = int(input("Enter your guess:")) # keeps track of the user's guess
    # checks that the user's guess is bigger than the price of the car
    if guess > price:
        print("Too high!")
    # checks that the user's guess is smaller than the price of the car
    elif guess < price:
        print("Too low!")
    # checks that the user's guess is equal to the price and that the amount of rounds exceeded 5
    elif guess == price and rounds > 5:
        print("It took", rounds, "guesses.")
        print("Too many guesses!")
        break
    # checks that the user's guess is equal to the price
    elif guess == price:
        print("It took", rounds, "guesses.")
        print("You won the car!")
        break
    rounds = rounds + 1 # increments the number of guesses
        
