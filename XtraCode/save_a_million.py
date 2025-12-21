# save_a_million.py

balance = 100.0 # account balance
taxed_balance = 0 # parallel taxed account

monthly_savings = float(input("Enter monthly savings:"))

annual_rate_pct = float(input("Enter APR")) # in percent

monthly_rate_pct = annual_rate_pct / 12 # in percent

month = 0 # Years account has been open

print("Month", "Balance", "Taxed Balance", sep="\t")

#loop until balance is at least $1M

while balance < 1000000 or taxed_balance < 1000000:
    month = month + 1
    balance = balance + monthly_savings # paycheck 1st of the month
    taxed_balance = taxed_balance + monthly_savings
    interest = balance * (monthly_rate_pct/100)
    taxed_interest = taxed_balance * (monthly_rate_pct/100)
    taxes = taxed_interest * 0.2
    balance = balance + interest
    taxed_balance = taxed_balance + taxed_interest - taxes
    if month % 12 == 0:
        print(month, "${:.2f}".format(balance), "${:.2f}".format(taxed_balance), sep = "\t")

print(month, "${:.2f}".format(balance),sep = "\t")
