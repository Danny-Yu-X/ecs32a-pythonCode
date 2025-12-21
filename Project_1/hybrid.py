# hybrid.py
# Danny Yu
# This program computes the five year costs of gas, a hybrid car, and the total cost of those components.

#The car price in dollars.
carPrice = float(input("Cost of car:"))
#Prompts the user for the miles driven per year
miles = int(input("Miles driven per year:"))
#The gas price per gallon in dollars
gasPrice = float(input("Cost of gas:"))
#The fuel efficiency in miles per gallon
fuelEfficiency = int(input("Fuel efficiency (mpg):"))
#The resale value of the car in dollars after five years
resaleValue = float(input("Estimated resale value after 5 years:"))
#Formula for calculating the five year gas cost
fiveYearGasCost = miles / fuelEfficiency * gasPrice * 5
#Outputs the five year gas cost
print("Five year gas cost:", fiveYearGasCost)
#Formula for the five year car cost
fiveYearCarCost = carPrice - resaleValue
#Outputs the five year car cost
print("Five year car cost:", fiveYearCarCost)
#Formula for the five year total cost
totalCost = fiveYearGasCost + fiveYearCarCost
#Outputs the five year total cost
print("Five year total cost:", totalCost)
