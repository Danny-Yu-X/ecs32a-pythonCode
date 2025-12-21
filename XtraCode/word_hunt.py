#word_hunt.py

filename = input("Enter filename")
infile = open(filename)

query = input("Enter query;")

query = query.lower()
word_count = 0
line_count = 0




for line in infile:
    line = line.rstrip("\n")
    #words = line.split()
    word_count = word_count + line.count(query)
    if query in line:
        print(line)
        line_count = line_count + 1

print("Word count:", word_count)
print("Line count:", line_count)
    
#not done lol
