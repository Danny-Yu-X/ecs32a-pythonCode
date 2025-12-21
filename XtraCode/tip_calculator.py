# tip_calculator

total = float(input("Enter total:"))
pct_tip = int(input("Enter % tip:"))
tip = total * (pct_tip/100)
total = total + tip
print("New total ${:.2f}".format(total))
