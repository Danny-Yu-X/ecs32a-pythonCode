# phone.py
# Danny Yu
# This program prompts the user to enter a phoone number in a specified format
# The program then validates or invalidates the entered phone number

#prompt user to enter a phone number
phone = input("Enter number as ### ###-####:")
#valides a phone number that is at most 13 characters long
valid = len(phone) <= 13
#the starting position of the phone number
pos = 0
#loops for the validity of the phone number at positions 0, 3, 7, and 8
# loops until the phone is not valid and the pos is 13
while valid and pos < 13:
    #checks that at position 0, it is a digit
    if pos == 0:
        valid = phone[pos] in "123456789"
    #checks that at position 3, it is a space
    elif pos == 3:
        valid = phone[pos] == " "
    #checks that at position 7, it is a dash
    elif pos == 7:
        valid = phone[pos] == "-"
    #checks that at position 8, it is a digit
    elif pos == 8:
        valid = phone[pos] in "123456789"
    #increment position by 1
    pos = pos + 1

if valid:
    print("Valid")
else:
    print("Invalid")






