# quiz_part1.py
# Danny Yu
# This program asks the user a question and prompts the user to enter a choice.
# The program then tells the user if they are correct or what the correct answer is.

#asks the user a question and provides multiple choices to choose from 
print("ART: Who painted 'The Persistance of Memory'?")
# answer choices to the question
print("a. Dali")
print("b. Munch")
print("c. Picasso")
#prompts the user to choose an answer by typing a, b, or c
answer = input("Enter your choice:") #stores the user's answer to the question
# checks if the user's answer is a
if answer == "a":
    print("Correct!") #outputs that the user's answer is correct
# checks that the answer is something other than a
else:
    print("The correct answer was a") # outputs the correct answer
    
