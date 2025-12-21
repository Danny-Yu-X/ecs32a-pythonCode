# starbucks_menu.py
#
# This program reads the starbuck menu and finds the
# item with the maximum calories and the minimum carbs

# Get the filename from the user (e.g. Starbucks.txt)
filename = input("Enter filename:")

# Open the file in filename for reading
# The open file will be put into the variable infile
# infile now contains a filehandle
infile = open(filename)

# Initialize the running statistics
# Similar to running_max/running_min in statistics.py
min_carbs = None
min_item = None

max_cals = None
max_item = None

# This next line reads one line from the input file
# line contains the header which we don't want to process
# in the loop.
line = infile.readline()

# The loops reads 
for line in infile:
    # line looks like this: 'Blueberry Muffin\t360\t52\n'

    # strip off whitespace on the ends
    line = line.strip()
    # line now looks like this: 'Blueberry Muffin\t360\t52'
    
    # Split line on the "\t" character and put it into three variables
    # item = 'Blueberry Muffin'
    # cals = '360'
    # carbs = '52'
    item, cals, carbs = line.split("\t")

    # convert cals and carbs from strings to numbers
    cals = int(cals)
    carbs = int(carbs)

    # update the running minimum carbs
    # this is similar to what we do in statistics.py 
    # but we also keep track of the item name
    if min_carbs == None or carbs < min_carbs:
        min_carbs = carbs
        min_item = item
        
    # update the running maximum calories
    if max_cals == None or cals > max_cals:
        max_cals = cals
        max_item = item

# Output the results
print("Max cals:", max_item, max_cals)
print("Min carbs:", min_item, min_carbs)
