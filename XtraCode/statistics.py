#statistics.py

#compute statistics on user entered values

running_count = 0
running_sum = 0
running_min = None
running_max = None

# Loop for numbers until the user enters "done"

while True:
    ans = input("Enter a number of 'done' to exit:")
    if ans == "done":
        break

    ans = float(ans)
    running_count = running_count + 1
    running_sum = running_sum + ans

    if running_min == None or ans < running_min:
        running_min = ans
    
    if running_max == None or ans > running_max:
        running_max = ans


print("Count:", running_count)
print("Sum:", running_sum)
print("Average:", running_sum/running_count)
print("Min:", running_min)
print("Max:", running_max)
print("Range:", running_max - running_min)
