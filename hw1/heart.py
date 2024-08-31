# heart.py
# Danny Yu
# This program prompts the user for their age and calculates the user's maximum heart rate and target heart rate range.

#age in years
age = int(input("Enter your age:"))
#Formula for calculating maximum heart rate in beats per minute
maximumHeartRate = 220 - age
#target heart rate ranges
#target heart rate that is 50% of maximum heart rate
targetHeartRate1 = maximumHeartRate * 0.50
#target heart rate that is 85% of maximum heart rate
targetHeartRate2 = maximumHeartRate * 0.85
#outputs the maximum heart rate in bpm.
#Also outputs the range of the user's target heart rate in bpm
print("Your maximum heart rate is", maximumHeartRate, "bpm")
print("Your target heart rate is", targetHeartRate1, "-", targetHeartRate2, "bpm")
