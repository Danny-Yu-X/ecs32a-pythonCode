# cash.py
# Danny Yu
# This program prompts the user to enter a file name and calculates the number of items in the file as well as the total sum dollars.


print("Automated cash register")

# prompts the user to enter a file name
file_name = input("Enter file of prices:")
# opens the file and creates a file handle
infile = open(file_name)
# keeps track of the number of items in the file
items = 0
# keeps track of the sum of the items
total = 0
#loops for each line in the file adding each line
#loops until the last line of the file
for line in infile:
    #converts the string to a float
    num = float(line)
    # adds each line to create a running sum
    total = total + num
    #increments the number of items each time there is a new line
    items = items + 1
    #outputs the total number of items and the sum in dollars
print("File contained", items, "items totaling", "${:.2f}".format(total))

    
    
    
    
    
