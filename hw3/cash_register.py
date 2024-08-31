#cash_register.py
# Danny Yu
# This program prompts the user to enter the cost for an item and repeats until the user just presses enter.
# Once the loop is finished, the program then outputs the number of items entered and calculates the total amount of the entered user costs in dollars.


print("Cash register (press enter to exit)")

items = 0 # keeps track of the number of items
running_sum = 0 # keeps track of the total amount of the entered costs
#loops the prompting of the user entering the cost in dollars until the user presses just the enter key
#iterates over items and the running sum
while True:
    item_cost_str = input("Enter item cost:")
    if item_cost_str == "": # when the user just types enter, loop terminates
        break


    item_cost_num = float(item_cost_str) # converts the string to a float
    
    running_sum = running_sum + item_cost_num # keeps track of the item costs
    
    items = items + 1 # increments items
#outputs the total amount of items and the running sum
print("You entered", items, "items totaling", "${:.2f}".format(running_sum))
    
