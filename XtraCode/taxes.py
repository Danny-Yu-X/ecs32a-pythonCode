# taxes.py
# Kristian Stevens
#
# Computes income taxes



# Income Thresholds
SINGLE_INCOME_THRESHOLD = 32000
MARRIED_INCOME_THESHOLD = 64000

# TAX Rates
TAX_RATE1 = 0.1
TAX_RATE2 = 0.25

# Get income
income = int(input("Enter income:"))

# Married or Single
married = input("Married (y/n)?") == "y"

# Compute single taxes
tax = 0
if not married:
    # Income under theshold
    if income <= SINGLE_INCOME_THRESHOLD:
        tax = income * TAX_RATE1
    # Income over theshold
    else:
        tax = SINGLE_INCOME_THRESHOLD * TAX_RATE1
        tax = tax + ((income - SINGLE_INCOME_THRESHOLD) * TAX_RATE2)
# Compute married taxes
else:
    # Income under theshold
    if income <= MARRIED_INCOME_THESHOLD:
        tax = income * TAX_RATE1
    # Income over theshold
    else:
        tax = MARRIED_INCOME_THESHOLD * TAX_RATE1
        tax = tax + (income - MARRIED_INCOME_THESHOLD) * TAX_RATE2

# Print formatted results  
print("You owe the IRS $" + "{:.2f}".format(tax))
