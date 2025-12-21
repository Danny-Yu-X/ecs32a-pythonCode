#reverse_lookup.py

phone_dir = {}

infile = open("phoneDir.txt")

for line in infile:
    line = line.strip()
    name, phone = line.split("\t")
    phone_dir[phone] = name

#print(phone_dir)

#loop 2
#loopkup values by key
while True:
    phone = input("Enter phone number or nothing to quit:")
    if phone == "":
        break
    if phone in phone_dir:
        print(phone, phone_dir[phone])
    else:
        print(phone, "not found")
