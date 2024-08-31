# change.py
# Danny Yu
# This program program calculates the minimum amount of quarters, dimes, nickels, and pennies for a specified amount of cents given by the user.

# prompts the user to enter a specified amount of cents
cents = int(input("Enter cents:"))

quarters = 25 # in cents
dimes = 10 # in cents
nickels = 5 # in cents
pennies = 1 # in cents

# calculates the total amount of quarters
total_quarters = cents // quarters
# calculates the leftover change
left_over_1 = cents - (total_quarters * quarters) 
# calculates the total amount of dimes
total_dimes = left_over_1 // dimes
# calculates the leftover change 
left_over_2 = left_over_1 - (total_dimes * dimes)
# calculates the total amount of nickels
total_nickels = left_over_2 // nickels
# calculates the remaining pennies
total_pennies = cents % (total_quarters * quarters + total_dimes * dimes + total_nickels * nickels)

print("The minimum coins for", cents, "cents are:")
#outputs the total quarters
print(total_quarters, "Quarters")
#outputs the total dimes
print(total_dimes, "Dimes")
#outputs the total nickels
print(total_nickels, "Nickels")
#outputs the total pennies
print(total_pennies, "Pennies")
