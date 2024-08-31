# pocket.py
# Danny Yu
# This program computes a user's pocket change by prompting the user to input the amount of quarters, dimes, nickels, and penniees they have.
# The program then adds the total of coins they have and outputs it for the user.

print("Compute your pocket change!")
# prompts the user to enter the amount of quarters
quarters = int(input("Quarters?")) # stores the amount in quarters
#prompts the user to enter the amount of dimes
dimes = int(input("Dimes?")) # stores the amount in dimes
# prompts the user to enter the amount of nickels
nickels = int(input("Nickels?"))# stores the amount in nickels
#promtps the user to input the amount of pennies
pennies = int(input("Pennies?"))# stores the amount in pennies
#calculates the total change in quarters
total_quarters = quarters * 0.25
#calculates the total change in dimes
total_dimes = dimes * 0.10
#calculates the total change in nickels
total_nickels = nickels * 0.05
#calculates the total change in pennies
total_pennies = pennies * 0.01
#calculates the total amount of change
total = total_quarters + total_dimes + total_nickels + total_pennies
#outputs the total amount in dollars
print("The total is", "${:.2f}".format(total))
