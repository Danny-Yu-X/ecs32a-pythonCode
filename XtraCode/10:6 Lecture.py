#"_" * 100 # prints the _ 100 times

#fahrenheit = input("Enter degrees Fahrenheit: ")


#fahr = int(input("Enter Degrees Fahrenheit: "))

#input("Do you like the number " + str(42) + "?")

#print("$", str(42))
#______________________________________
# parrot.py
#Danny Yu

#Echo user input
text = input("")
print("You entered ", text)

# stamps.py

STAMP_PRICE = 55

dollars = input("Enter dollars: ")

dollars = int(dollars)

pennies = dollars * 100

stamps = pennies // STAMP_PRICE

change = pennies % STAMP_PRICE

print("stamps:", stamps)

print("change:", change)
