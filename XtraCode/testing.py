s = input("Enter a price:")
try:
    float(s.replace("$", ""))
except:
    print("That's not a price!")
