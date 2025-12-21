# trycat.py
# Danny Yu
# This program prompts the user to enter a file name and outputs the contents/lines from the file to the user
# If the file does not exist, it will prompt the user to enter another one


#loops until the user enters a file name that exists
while True:
    #prompts the user to enter a file name
    file_name = input("Enter a file name to open:")
    try:
    # opens the file to read and creates a file handle assigned to infile
        infile = open(file_name, "r")
        break
    # checks that the file does not exist
    except:
        print("Could not open '" + file_name + "'")
        continue
#loops for each line in the file/until the last line of the file and outputs the contents of each line for the user
for line in infile:
    #strips off any whitespace characters in the file
    line = line.strip()
    #outputs each line in the file
    print(line)
