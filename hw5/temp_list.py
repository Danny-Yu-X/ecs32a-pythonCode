#temp_list.py
#Danny Yu
#This program prompts the user to enter a file name, adds the temps to a growing list, and outputs list.

#prompts the user to enter a file name
file_name = input("Temperature anomaly filename:")
#opens the file to read and creates a file handle stored in infile
infile = open(file_name, "r")
#reads the header of the file and ignores it in the output
infile.readline()

# keeps track of the growing list of temperatures
temp_list = []

#loops for each line in the file, removiing newline characters, extracting year and temp, and adds to the temp list
#loops until the last line of the file
for line in infile:
    #remove any newline characters after each line
    line = line.strip()
    #split on the comma to extract year and temperature
    year,temp = line.split(",")
    #convert temp to a float
    temp = float(temp)
    #add to the list of temp
    temp_list.append(temp)
    
#outputs the temperature list
print(temp_list)
    
#closes the file
infile.close()

