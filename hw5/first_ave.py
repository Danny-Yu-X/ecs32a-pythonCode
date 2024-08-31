#first_ave.py
#Danny Yu
#This program prompts the user to enter a file name and a window size, adds the temps to a growing list, and takes the average of the temps in the list with the corresponding year for output.

#prompts the user to enter a file name
file_name = input("Temperature anomaly filename:")
#opens the file to read and creates a file handle stored in infile
infile = open(file_name, "r")
#reads the header of the file and ignores it in the output
infile.readline()
#promprts the user to enter a window size
k = int(input("Enter window size:"))

# keeps track of the growing list of temperatures
temp_list = []

#loops for each line in the file, removiing newline characters, extracting year and temp, and adds to the temp list and takes the average of the temps in that list
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
    #set the window size as the index
    index = k
    #year is now the starting year plus the winsow size for the year of the average
    year = 1880 + index
    #calculate moving average for first valid index in list
    ave = sum(temp_list[index-k:index+k+1]) / (2*k+1)
    #output the year and average for first valid index
print("{:.0f},".format(year) + "{:.4f}".format(ave))
    
#closes the file
infile.close()

