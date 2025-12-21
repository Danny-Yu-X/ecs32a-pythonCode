#

"""outstr = ""

instr = input("Input")
instr = instr.upper()
for c in instr:
    #if c is a vowel change it to a blank
    if c in "AEIOUY":
        c = "_"
    outstr = outstr + c
print("Output:", outstr)"""

#

"""instr = input("Enter a string:")
length = 0
num_upper = 0
num_lower = 0
num_vowel = 0
num_cons = 0
for c in instr:
    #Update our running values
    length = length + 1
    if c.isupper():
        num_upper = num_upper + 1
    if c.islower():
        num_lower = num_lower + 1
    c = c.upper()
    if c in "AEIOUaeiou":
        num_vowel = num_vowel + 1
    else:
        num_cons = num_cons + 1

print("Length:", length)
print("Uppercase:", num_upper)
print("Lowercase:", num_lower)
print("Vowels:", num_vowel)
print("Consonants:", num_cons)"""

"""phone= input("Enter a number as (123)456-7890:")
valid = len(phone) == 13
pos  = 0
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



