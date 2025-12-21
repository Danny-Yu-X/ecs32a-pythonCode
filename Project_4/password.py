# password.py
# Danny Yu
# This program asks the user to input a password
# The program checks for the password's length, number of uppercase and lowercase characters
# The program also checks for the number of digits and special characters and outputs whether or not the password has these components.

#get password from user
password = input("Enter password:")

num_length = 0 # keeps track of the password length
num_lower = 0 # keeps track of the number of lowercase characters
num_upper = 0 # keeps track of the number of uppercase characters
num_digit = 0 # keeps track of the number of digits numbered 0-9
num_special = 0 # keeps track of the number of special characters (!@#$%&)

# loop over each letter in password
# loops until the last character of the password
for letter in password:
    num_length = num_length + 1 #increments the password length
    # Count lower and upper case
    if letter.islower():
        num_lower = num_lower + 1 # increments the number of lowercase characters
    if letter.isupper():
        num_upper = num_upper + 1 #increments the number of uppercase characters
    #Count digits and special characters
    if letter in "0123456789":
        num_digit = num_digit + 1 #increments the number of digits numbered 0-9
    if letter in "!@#$%&":
        num_special = num_special + 1 #increments the number of special characters
#checks to see if the password is at least 8 characters long   
if num_length >= 8:
    print("Has length")
#checks to see if password has at least one lower case character
if num_lower >= 1:
    print("Has lower case")
#checks to see if password has at least one upper case character
if num_upper >= 1:
    print("Has upper case")
#checks to see if password has at least one digit number 0-9
if num_digit >=1:
    print("Has digit")
#checks to see if password has at least one of the special characters (!@#$%&)
if num_special >= 1:
    print("Has special")
