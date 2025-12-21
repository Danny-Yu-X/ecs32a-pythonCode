# loop.py
# Loop for correct input

# correct input for the quiz program is a, b, or c

#looop until uou get valid input
"""ans = input("Enter your choice:")
while not (ans == "a" or ans == "b" or ans == "c"):
    print("You must enter a, b, or c")
    ans = input("Enter your choice:")
print(ans)"""

#__________________________

#nested_loop.py

row = 1

width = 10
height = 10

while row <= height:
    column = 1
    while column <= width:
        print("{:3.0f}".format(row * column), end ="")
        column = column + 1
    print()
    row = row + 1
