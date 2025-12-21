# digits.py
# Danny Yu
# This program prompts the user to enter a phone number and removes/hides any spaces, parentheses, and dashes entered
# The program then outputs the phone number only containing digits 

digit_string = "" # keeps track of the digits in the phone number
remove = "()- " # these are what would be removed or stripped off from the phone number

#prompts the user to enter a phone number
phone = input("Enter phone number:")

#loops for each digit in the sequence of phone
#loops until the last digit in the phone number 
for digit in phone:
    #checks to see if the digit is space, parenthesis, or a dash and removes it
    if digit in remove:
        digit = "" # hides the space, parenthesis or dash
    digit_string = digit_string + digit # adds the next digit in order
#ouputs the new phone number only containing digits
print("Digit string:", digit_string)
