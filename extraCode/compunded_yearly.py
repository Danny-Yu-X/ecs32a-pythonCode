# compounded_yearly.py

balance = 100.0 # account balance

annual_rate_pct = 7 # in percent

monthly_rate_pct = annual_rate_pct / 12 # in percent

month = 0 # Years account has been open


#loop until year is 50 i.e. loop 50 years

while month < 50 * 12:
    month = month + 1
    interest = balance * (monthly_rate_pct/100)
    balance = balance + interest

print("After", month//12, "years the balance is", "${:.2f}".format(balance))
