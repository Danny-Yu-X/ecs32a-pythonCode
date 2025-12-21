# pythagorean _tripples.py

#Find a < b < c where a,b, and c are <= 100
# and a a**2 + b**2 == c**2
"""height = 10
width = 20

for a in range(1,101):
    for b in range(a+1,101):
        for c in range(b+1,101):
            if a**2 + b**2 == c**2:
                print(a,b,c)"""
 
#__________________

"""try:
    ans = int(input("Enter an integer:"))
except:
    
print("You entered", ans)"""

#________________


"""while True:
    fahr = input("Enter degrees F:")
    try:
        fahr  = float(fahr)
        break
        
    except:
        print("Didn't understand you, enter a number!")
        continue
celsius = (fahr - 32) * 5/9
print(fahr, "F is", celsius, "C")"""


#______

"""while True:
    ans = input("Enter an integer between 1 and 100:")
    try:
        ans = int(ans)
    except:
        print("You didn't enter an integer")
        continue
    if ans >=1 and ans <= 100:
        break
    else:
        print("Not in range")
print("You entered", ans)"""

#_____________

"""import sys

while True:
    filename = input("Enter filename:")
    try:
        open(filename)
        break
    except:
        print("Could not find", filename)
        print("I give up")
        sys.exit()"""

#_____

#waterfall.py

import random

CURSOR = "|||||||||"

SCREEN_WIDTH = 60

START_POS = SCREEN_WIDTH // 2

currnet_pos = START_POS
try:
while True:
    current_pos = curent_pos + random.choice([-1,1])
    print(" "*current_pos+ CURSOR)
except:
    print("Thank you! Done!")


    
