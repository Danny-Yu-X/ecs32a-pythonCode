# parrot.py
# Danny Yu
# This program outputs the user's input in all caps until the user inputs "quiet"


#loops for user input and outputs it in all caps
#loop terminates when the user inputs "quiet"

while True:
    line = input(">") #get user input

    new_line = line.upper() #convert line to all uppercase
    
  #checks if the user inputs "quiet" and breaks out the loop
    if new_line in "QUIET":
        break
    else:
        #outputs the user's input in all caps
        print(new_line)
        continue #loops the program again
     




