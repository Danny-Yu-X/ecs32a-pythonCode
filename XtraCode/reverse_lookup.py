# reverse_lookup.py
# ECS 32A
# Reverse phone number lookup

# First loop reads the phone book and creates the index
filename = "phoneDir.txt"
infile = open(filename)

rev_lookup = {} # maps phone numbers to names

for line in infile:
    line = line.strip()
    name, phone = line.split("\t")
    rev_lookup[phone] = name

# Uncomment to check to see if the dictionary looks OK
# print(rev_lookup)

# second loop queries phone numbers to look up
while True:
    phone = input("Enter a phone number or nothing to exit:")
    if phone == "":
        break
    if phone in rev_lookup:
        name = rev_lookup[phone]
        print(name)
    else:
        print("Not found")
    

