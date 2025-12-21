filename = input("Enter file:")
infile = open(filename)
filename = input("Output filename:")
outfile = open(filename, "w")

for line in infile:
    line = line.strip()
    line = line.replace("/t", ",")
    outfile.wrtie(line)
outfile.close()
    
