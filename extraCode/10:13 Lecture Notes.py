"""temp = int(input("Enter temp:"))

if temp <= 0:
    print("Solid")
elif temp < 100:
    print("Liquid")
else:
    print("Gas")"""
#_____________________________________

#chained conditional

#cel2eng.py

#Freezing cold: 0 degrees or below
"""temp = int(input("Enter degrees C:"))

if temp <= 0:
    print("Freezing cold")

#Cold: below 10
elif temp < 10:
    print("Cold")
#Cool: below 15
elif temp < 15:
    print("Cool")
#Nice: between 15 and 25
elif temp <= 25:
    print("Nice")
#Super hot: above 35
elif temp >35:
    print("Super hot")
#Hot: Above 30
elif temp > 30:
    print("Hot")
#Warm: above 25
elif temp > 25:
    print("Warm")"""
#________________________________________
"""x = 9
if x > 0 and x < 10:
    print("Single digit positive")"""
#_______________________________________

#taxes.py

SINGLE_LIMIT = 32000
MARRIED_LIMIT = 64000
RATE1 = 0.1
RATE2 = 0.25

income = float(input("Enter income:"))
marital_status = input("Are you married (y/n)?")
tax = 0
#Single case
if marital_stats == "n"

    if income <= SINGLE_LIMIT:
        tax = RATE1 * income
    else:
        tax = RATE1 * SINGLE_LIMIT
        tax = tax + RATE2 * (income - SINGLE_LIMIT)
#Married case
else:
    if income <= MARRIED_LIMIT:
        tax = RATE1 * income
    else:
        tax = RATE1 * MARRIED_LIMIT
        tax = tax + RATE2 * (income - MARRIED_LIMIT)

print("Tax", tax)

