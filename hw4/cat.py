# cat.py
# Danny Yu
# This program prompts the user to enter a file name and outputs the contents/lines from the file to the user

#prompts the user to enter a file name
file_name = input("Enter a file name to open:")
# opens the file to read and creates a file handle assigned to infile
infile = open(file_name, "r")
#loops for each line in the file/until the last line of the file and outputs the contents of each line for the user
for line in infile:
    #strips off any whitespace characters in the file
    line = line.strip()
    #outputs each line in the file
    print(line)

