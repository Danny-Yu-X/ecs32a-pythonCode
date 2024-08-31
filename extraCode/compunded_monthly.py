# compounded_monthly.py

balance = 100.0 # account balance

annual_rate_pct = 7 # in percent

year = 0 # Years account has been open


#loop until year is 50 i.e. loop 50 years

while year < 50:
    year = year + 1
    interest = balance * (annual_rate_pct/100)
    balance = balance + interest

print("After", year, "years the balance is", "${:.2f}".format(balance))
