# circle.py
# Danny Yu
# This program calculates the circumference and area of a circle. 

#prompts user for the radius of a circle as a floating value
radius = float(input("Enter radius:"))
#diameter of a circle
diameter = 2 * radius
#outputs the diameter of the circle
print("Diameter", diameter)
#formula for the circumference of a circle. 3.14159 is the value of pi.
circumference = 3.14159 * diameter
#outputs the circumference of the circle
print("Circumference", circumference)
#formula for the area of a circle
area = 3.14159 * radius**2
#outputs the area of the circle
print("Area", area)
