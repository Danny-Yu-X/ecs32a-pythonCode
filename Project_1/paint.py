# paint.py
# Danny Yu
# Calculates the number of cans of paint needed to cover four walls of a rectangular room.


print("Paint coverage estimator")
# length in inches
length = int(input("Length of room in inches:"))
#width in inches
width = int(input("Width of room in inches:"))
#average height in inches
averageHeight = int(input("Average height of room in inches:"))
#calculates the area in square inches of the four walls
area = 2 * (averageHeight * length) + 2 * (averageHeight * width)
#calculates the number of cans required as a floating point number
cans = area / 144 / 100
#converts the floating point result cans to an integer
cansFinal = int(cans) + 1
#outputs the number of cans of paint needed
print("You'll want", cansFinal, "cans.")


