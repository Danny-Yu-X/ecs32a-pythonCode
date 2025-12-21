# divide.py
# Danny Yu
# This program divides two numbers and outputs the quotient and remainder.

# Prompts the user for the dividend
number1 = int(input("Enter a number:"))
# Prompts the user for the divisor
number2 = int(input("Enter a number to divide that by:"))
# Calculates the quotient as an integer by dividing the dividend by the divisor
quotient = number1 // number2
# Calculates the remainder
remainder = number1 % number2
# Outputs the quotient and remainder for the user
print(number1, "divided by", number2, "is", quotient, "with", remainder, "remaining")
