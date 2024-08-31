#statistics.py

while True:
    filename = input("Open filename:")
    try:
        infile = open(filename)
    except:
        print("File not found")
    break
    
running_count = 0
running_sum = 0
running_min = None
running_max = None

for line in infile:
    line = line.strip()
    num = float(line)

    running_count = running_count + 1
    running_sum = running_sum + num
    if running_sum == None or num < running_min:
        running_min = num

    if running_max == None or num > running_max:
        running_max = num

print("Count:", running_count)
print("Ave:", running_sum / running_count)
print("Min:", running_min)
print("Max", running_max)
