# statistics_list.py

#Compute statistics on a file of numbers using a list



file_name = input("Enter a file of scores:")

infile = open(file_name)

nums = [] # seed a list of numbers

#loop over the numbers in the file
for line in infile:
    line = line.strip()
    num = float(line)
    nums.append(num)
print("Length", len(nums))
print("Sum:", sum(nums))
print("Min:", min(nums))
print("Max:", max(nums))
print("Average:", sums(nums)/len(nums))

#calculate median
nums.sort()
#Case 1: list is odd length
if len(nums) % 2 ==1 :
    median = nums[len(nums)//2]

#Caes 2: list is even length
else:
    median = (nums[len(nums) // 2 ] + nums[len(nums) // 2 - 1])/2

    print
