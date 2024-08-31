# bmi.py
# Danny Yu
# This program calculates the user's BMI by obtaining the user's height and weight.

# Prompts for the user's height in inches
height = float(input("Enter height in inches:"))
# Prompts for the user's weight in pounds
weight = float(input("Enter weight in pounds:"))
# BMI formula that calculates BMI given a height in inches and weight in pounds.
BMI = weight / height**2 * 703
#outputs the user's BMI
print("BMI:", BMI)
