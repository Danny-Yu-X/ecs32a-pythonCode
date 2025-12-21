# mileage.py
# Danny Yu
# This program prompts the user to input miles driven and gallons to output the mileage.
# This program also loops untl the user inputs the enter key, which outputs the average mileage.


print("Your Personal Fuel Economy")


running_sum_miles = 0 # keeps track of the amount of miles as they are entered

running_sum_gallons = 0 # keeps track of the amount of gallons as they are entered

# loops for user input for miles and gallons and outputs the mileage
# If the user clicks the enter key, the loop terminates and outputs the average mileage
while True:
    #prompts the user to input miles and stores it
    miles_str = input("Number of miles traveled (or enter to exit):")
    #checks to see if the user inputs the enter key and terminates loop
    if miles_str == "":
        break
    #prompts the user to input gallons and stores it
    gallons = int(input("Number of gallons needed:"))
    #converts miles from a string to an integer
    miles_num = int(miles_str)
    #calculates the mileage by dividing the miles by the gallons
    mileage = miles_num / gallons
    #outputs the mileage
    print("Mileage this tank =", "{:.1f}".format(mileage))
    #as the loop continues, the number of miles accumulates as a sum
    running_sum_miles = running_sum_miles + miles_num
    # as the loop continues, the number of gallons accumulates as a sum
    running_sum_gallons = running_sum_gallons + gallons
#outputs the average mileage by dividing the total miles by the total galons
print("Average mileage =", "{:.1f}".format(running_sum_miles / running_sum_gallons))
