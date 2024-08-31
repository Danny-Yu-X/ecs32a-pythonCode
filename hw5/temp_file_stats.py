#temp_file_stats.py
#Danny Yu
#This program prompts the user to enter a file name and outputs the minimum and maximum tempertaures with their corresponding year in the file.


#prompts the user to enter a file name
file_name = input("Temperature anomaly filename:")
#opens the file to read and creates a file handle stored in infile
infile = open(file_name, "r")


min_temp = None # keeps track of the minimum temperature
min_year = None # keeps track of the year with the minimum temp
max_temp = None # keeps track of the maximum temperature
max_year = None # keeps track of the year with the max temp

#reads the header of the file and ignores it in the output
infile.readline()
#loops for each line in the file, removiing newline characters, extracting year and temp, and finds the min and max temps with their year.
#loops until the last line of the file
for line in infile:
    #remove any newline characters after each line
    line = line.strip()
    #split on the comma to extract year and temperature
    year,temp = line.split(",")
    #converts the temp to a float
    temp = float(temp)
    #convert year to an int
    year = int(year)
    #checks that miin temp is none or that the temp is less than the min temp
    if min_temp == None or temp < min_temp:
        min_temp = temp
        min_year = year
    #checks that max temp is none or that the temp is greater thanthe max temp
    if max_temp == None or temp > max_temp:
        max_temp = temp
        max_year = year
#outputs the min and max temp of the file with corresponding year
print("Min temp:", min_temp, "in", min_year)
print("Max temp:", max_temp, "in", max_year)

#closes the file
infile.close()

