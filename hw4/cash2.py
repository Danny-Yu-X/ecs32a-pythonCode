# cash2.py
# Danny Yu
# This program prompts the user to enter a file to open
# This program then calculates the total number of items and sum in dollars in the file.
# If the line cannot be converted to a floating point number, the line is skipped and the program moves on to the next line in the file.

print("Automated cash register")

#prompts the user to enter a file
file_name = input("Enter file of prices:")
#opens the file and creates a file handle
infile = open(file_name)
#keeps track of the number of items in the file
items = 0
# keeps track of the total sum of the items in dollars in the file
total = 0
#loops for each line in the file, adding the lines that can be convereted to a floating point number and adding those items up
#loops until the last line of the file
# if the line cannot be converted to a floating point number, it is skipped and moves on to the next line
for line in infile:
    try:
        #replaces the $ sign with an empty string to mask out the dollar sign
        new_line = line.replace("$", "")
        #converts the new line without a dollar sign to a floating point num
        num = float(new_line)
        # adds the floating point numbers up
        total = total + num
        # increments the total items if the line is a floating point
        items = items + 1
    except:
        #if the line is not a floating point num, it gets skipped
        #program continues to the next line
        continue
#outputs the total number of items and the sum of the items in dollars
print("File contained", items, "items totaling", "${:.2f}".format(total))

