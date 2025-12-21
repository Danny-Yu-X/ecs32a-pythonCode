# tip.py
# Danny Yu
# This program prompts the user for a total amount of dollars.
# This program then calculates the tip in dollars by iteratiing through 15 percent to 25 percent tip.


# prompts the user to enter a total amount in dollars
total = float(input("Enter total:")) # keeps track of the total amount of dollars

# the tip in percent
tip = 15
# interates over the tip
# loop from 15 to 25 percent and outputs the percent tip and the tip in dollars
# loop stops when tip reaches 26 percent
while tip <= 25:
    total_tip = tip * total / 100 # calculates the tip in dollars
    print("A", "{:.0f}%".format(tip), "tip is", "${:.2f}".format(total_tip))
    tip = tip + 1


