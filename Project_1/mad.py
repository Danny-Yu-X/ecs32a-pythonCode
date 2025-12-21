# mad.py
# Danny Yu
# This program asks the user for an adjective, noun, plural noun, place, and body part. Then the program stores those answers and then puts them into a story for the user like the Mad Libs game. 



# asks the user for an adjective and stores it.
adjective = input("Enter an adjective:")
# asks the user for a noun and stores it.
noun = input("Enter a noun:")
#asks the user for a plural noun and stores it.
pluralNoun = input("Enter a plural noun:")
# asks the user for a place and stores it.
place = input("Enter a place:")
# asks the user for a body part and stores it.
bodyPart = input("Enter a part of the body:")
#outputs the fragmented story from the Mad Libs game with the user's inputs.
print("\nThere are many", adjective, "ways to choose a", noun, "to read.")
print("You could ask recommendations from your friends and", pluralNoun + ".")
print("If they are no help, head to your local library or", place, "and browse the shelves\nuntil something catches your", bodyPart + ".")
