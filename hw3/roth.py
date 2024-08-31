# roth.py
# Danny Yu
# This program prompts the user to enter an initial deposit and an annual percent rate.
# This program then calculates the amount of time in years in takes to double the investment with the specified APR by looping until the initial deposit doubles.


# prompts the user for the initial Roth IRA deposit in dollars
initial_deposit = float(input("Enter an initial Roth IRA deposit amount:")) # keeps track of the inital deposit
# prompts the user for the annual percent rate
annual_pct_rate = float(input("Enter an annual percent rate of return:"))# keeps track of the APR

#The doubled value of the initial deposit
initial_double = initial_deposit * 2

year = 0 # keeps track of the time in years
# loops the interest added to the initial deposit until the deposit passes double its initial value.
# the loop terminates when the initial deposit passes double its value
# iterates over the year
while True:
    #checks to see if the initial deposit is double in size
    if initial_deposit >= initial_double:
        break
    #calculates the interest by multiplying the initial deposit by the APR divided by 100
    interest = initial_deposit * (annual_pct_rate / 100)
    #adds the accumulated interest to the initial deposit
    initial_deposit = initial_deposit + interest
    #increments the year
    year = year + 1
    #outputs the new balance with respect to the year
    print("Value after year", "{:.0f}:".format(year), "${:.2f}".format(initial_deposit))
#outputs the year when the investment doubles
print("It will take", year, "years to double your investment with a", "{:.0f}%".format(annual_pct_rate), "APR.")


