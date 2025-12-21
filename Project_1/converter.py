# converter.py
# Danny Yu
# This program prompts the user to enter a character and converts the character to its corresponding integer and binary representations. 

#Prompts the user to input a character.
character = input("Enter a character:")
#Converts the entered character into an integer
num = ord(character)
#Converts the integer to a string representation of a binary number
binary = bin(num)
#Outputs the typed character, the corresponding integer, and the binary version of that character.
print(character, "corresponds to the integer", num, "which is", binary, "in binary.")
