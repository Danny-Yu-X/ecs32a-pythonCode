#Traversing a string using a definite while loop

"""i = 0
fruit = "banana"
while i < len(fruit):
    letter = fruit[i]
    print(letter)
    i = i + 1"""

#same idea but with a for loop

"""fruit = "rock"

for letter in fruit:
    print(letter)"""

#slicing

"""s = "Spoon and Fork"
print(s[0:2])
print(s[11:14])
print(s[:2]+s[11:])
print(s[0:-1])"""

#Get a differnt string

"""name = "monty"
name = "M" + name[1:]
print(name)"""

#replace part of string
"""line = "I am."
new_line = line.replace("I ","Sp")
print(new_line)"""

# reverse.py
"""reverse = ""
forward = input("Forward: ")
for c in forward:
    reverse = c + reverse
print("Reversed:", reverse)"""

# word_quiz.py
"""with_blanks = ""
missing = "AEIOU" # Mask these letters out
forward = input("Enter a word to mask: ")
forward = forward.upper()
for c in forward:
    if c in missing:
        c = "_"
    with_blanks = with_blanks + c
print("Can you guess the word:", with_blanks)"""

# word_stats.py
# ECS32A
#
# Print statistics for a single word 
"""word = input("Enter a word:")

num_vowels = 0
num_consonants = 0
num_upper = 0
num_lower = 0

# loop over each letter in word
for letter in word:
    # Count upper and lower case
    if letter.isupper():
        num_upper = num_upper + 1
    if letter.islower():
        num_lower = num_lower + 1
    # Switch everything to lower case
    # for the next comparisons
    letter = letter.lower()   
    # Count vowels and consonants    
    if letter in "aeiou":
        num_vowels = num_vowels + 1
    else:
        num_consonants = num_consonants + 1
print("Length:",len(word))        
print("Uppercase:",num_upper)
print("Lowercase:",num_lower)
print("Vowels:",num_vowels)
print("Consonants:",num_consonants)"""

#validate_phone.py

"""phone = input("Enter number as (123)123-1234:")        
valid = len(phone) == 13
pos = 0
while valid and pos < 13:
    if pos == 0:
        valid = phone[pos] == "("
    elif pos == 4:
        valid = phone[pos] == ")"
    elif pos == 8:
        valid = phone[pos] == "-"
    else:
        valid = phone[pos].isdigit()
    pos = pos + 1

if valid:
    print("Valid")
else:
    print("Invalid")"""

# opening a file
"""infile = open("nums.txt")
outfile = open("song.txt", "w")"""

#writing a file

"""outfile = open("song.txt", "w")
line = "I'm a lumberjack and I'm OK"
print(line)
outfile.write(line"\n")
outfile.close()"""

#write_song.py

#open file
"""outfile = open("song.txt", "w")
line = "I'm a lumberjack and I'm OK"
print(line)
#write line to file
outfile.write(line+"\n")
line = "I sleep all night and I work all day"
print(line)
#write line to file
outfile.write(line+"\n")
#close file
outfile.close()"""

#write_nums.py

"""import random
num_lines = int(input("How many numbers? "))
largest = float(input("Largest number? "))
filename = input("Output file name:")
outfile = open(filename, "w")
for i in range(num_lines):
    # random floating point between 0 and 1
    n = random.random()
    # change the range from 0 to largest
    n = n * largest
    # create output line
    line = str(n) + "\n"
    # write output line and print to screen
    outfile.write(line)
    print(line, end = "")
outfile.close() # close the file"""


#the for loop for reading a file
# read this as "foreach line in the input file"

"""infile = open("nums.txt")
for line in infile:
    line = line.strip()
    print(line)"""

#read_nums.py

# input filename
"""file_name = input("Enter filename:")
# file opened for reading
infile = open(file_name, "r")
for line in infile:
   # strip whitespace from ends
   line = line.strip()
   print(line)"""
#statistics_file.py
#see statistics_file.py on canvas

"""# get filename from user
filename = input("Enter input filename:")
# open input filehandle
infile = open(filename)
# for loop reads numbers from the file
for line in infile:
    # strip whitespace from end of input string
    line = line.strip()
    # convert to floating point
    in_num = float(line)"""
#looping until a file can be opened
"""while True:
    filename = input("Enter the file name: ")
    try:
        infile = open(filename)
    except:
        print("That file could not be opened!")
        continue
    break
print(filename,"is open")"""

#ignoring the first line

# open the menu file
"""infile = open("Starbucks.txt")
# read one line of the file   infile.readline()

(item,calories,carbs) = line.split("\t")
print(item)
print(calories)
print(carbs)"""

#starbucks_menu.py on canvas

#Writing a CSV file

"""outfile = open("Names.csv","w")
outfile.write("Last,First\n") # column header
# Keep asking the user for names to write to
# the output file, loop until they press enter
while True:
    first = input("Enter first name:")
    if first == "":
        break
    last = input("Enter last name:")
    outfile.write(last + "," + first + "\n")
outfile.close()"""

# Reading a CSV file

"""infile = open("Names.csv","r")
infile.readline() # ignore the header
for line in infile:
    # strip whitespace off ends
    line = line.strip()
    # extract into variables
    last,first = line.split(",")
    print(first, last)
infile.close()"""

print("hello world")




