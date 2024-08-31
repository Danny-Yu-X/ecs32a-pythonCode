#write_nums.py
import random


num_scores = int(input("How many scores?"))

# Open a filehandle for writing
outfile = open("nums.txt", "w")


for i in range(num_scores):
    score = random.random()
    socre = score * 100
    score_str = "{:.1f}".format(score)
    outfile.write((score_str)+"\n")
outfile.close()
