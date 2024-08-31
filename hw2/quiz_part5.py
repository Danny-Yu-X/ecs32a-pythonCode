# quiz_part5.py
# Danny Yu
# This program asks the user seven questions and prompts the user to choose an answer to each one.
# The program then tells the user if their answer is correct or it tells the user the correct answer.
# The program also keeps track of the user's score and tells the user their score in the end.
# This program then provides a messege for the user based on their score. 

score = 0 # keeps track of the user's score

# asks the user the first question
print("ART: Who painted 'The Persistance of Memory'?")
#answer choices to the first question
print("a. Dali")
print("b. Munch")
print("c. Picasso")
#prompts the user to enter a choice
answer1 = input("Enter your choice:") # stores the user's answer for the first question
#checks that the user's answer is a
if answer1 == "a":
    score = score + 1 # adds one to the current score
    print("Correct!") #outputs that the user's answer is correct
    
#checks that the user's answer is something other than a
else:
    print("The correct answer was a") #outputs the correct answer
# asks the user the second question
print("ENTERTAINMENT: How many oscars did Hitchcock win?")
#answer choices to the second question
print("a. None")
print("b. One")
print("c. Two")
#prompts the user to enter a choice
answer2 = input("Enter your choice:") # stores the user's answer for the second question
#checks that the user's answer is a
if answer2 == "a":
    score = score + 1 # adds one to the current score
    print("Correct!") #outputs that the user's answer is correct
#checks that the user's answer is something other than a
else:
    print("The correct answer was a") #outputs the correct answer
# asks the user the third question
print("SCIENCE: Which dinosaur is most closely related to the pelican?")
#answer choices to the third question
print("a. Velociraptor")
print("b. Stegosaurus")
print("c. Pterodactyl")
#prompts the user to enter a choice
answer3 = input("Enter your choice:") # stores the user's answer for the third question
# checks that the user's answer is a
if answer3 == "a":
    score = score + 1 # adds one to the current score
    print("Correct!") # outputs that the user's answer is correct
# checks that the user's answer is someting other than a
else:
    print("The correct answer was a") #outputs the correct answer
# asks the user the fourth question
print("HISTORY: Which of the following was not invented in Baja California?")
# answer choices to the fourth question
print("a. Margaritas")
print("b. Chocolate")
print("c. Caesar Salad")
#prompts the user to enter a choice
answer4 = input("Enter your choice:") # stores the user's answer for the fourth question
# checks that the user's answer is b
if answer4 == "b":
    score = score + 1 # adds one to the current score
    print("Correct!") # outputs that the user's answer is correct
#checks that the user's answer is something other than b
else:
    print("The correct answer was b") #outputs the correct answer
# asks the user the fifth question
print("SCIENCE AND NATURE: Can pigs swim?")
#answer choices to the fifth question
print("a. Yes")
print("b. No")
print("c. Only in salt water")
# prompts the user to enter a choice
answer5 = input("Enter your choice:") # stores the user's answer for the fifth question
# checks that the user's answer is a
if answer5 == "a":
    score = score + 1 # adds one to the current score
    print("Correct!") #outputs that the user's answer is correct
# checks that the user's answer is something other than a
else:
    print("The correct answer was a") # outputs the correct answer
# asks the user the sixth question
print("SPORT AND LEISURE: What color is the middle Olympic ring?")
# answer choices to the sixth question
print("a. Red")
print("b. Blue")
print("c. Black")
# prompts the user to enter a choice
answer6 = input("Enter your choice:") # stores the user's answer for the sixth question
# checks that the user's answer is c
if answer6 == "c":
    score = score + 1 # adds one to the current score
    print("Correct!") #outputs that the user's answer is correct
# checks that the user's answer is something other than c
else:
    print("The correct answer was c") #outputs the correct answer
# asks the user the Genius question
print("GENIUS: In ancient Rome, what is L divided by X?")
# prompts the user to put an answer
answer7 = input("Enter your answer:") # stores the user's answer for the genius question
# checks that the user's answer is V or 5
if answer7 == 'V' or answer7 == '5':
    score = score + 1 # adds one to the current score
    print("Correct!") # outputs that the user's answer is correct
# checks that the user's answer is something other than V or 5
else:
    print("Correct answers were 5 or V")# outputs the correct answer
#outputs the total score
print("Your final score is", score)
# checks that the total score is from 0 through 2
if score >=0 and score <= 2:
    print("You were unlucky!")
# checks that the total score is from 3 through 4
elif score >=3 and score <=4:
    print("At least you did better than chance!")
# checks that the total score is from 5 through 6
elif score >= 5 and score <= 6:
    print("Excellent!")
# checks that the score is 7
elif score == 7:
    print("Genius!")
