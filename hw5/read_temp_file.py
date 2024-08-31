#read_temp_file.py
#Danny Yu
#This program prompts the user to enter a file name and outputs the years and corresponding temperatures in that file.


#prompts the user to enter a file name
file_name = input("Temperature anomaly filename:")
#opens the file to read and creates a file handle stored in infile
infile = open(file_name, "r")
#reads the header of the file and ignores it in the output
infile.readline()
#loops for each line in the file, removiing newline characters, extracting year and temp, and outputting the year and temperature
#loops until the last line of the file
for line in infile:
    #remove any newline characters after each line
    line = line.strip()
    #split on the comma to extract year and temperature
    year,temp = line.split(",")
    #outputs the year and corresponding temperature
    print(year, float(temp))
    #closes the file
infile.close()

