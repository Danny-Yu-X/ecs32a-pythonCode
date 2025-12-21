# tsv_to_csv.py
# ECS32A
#
# Convert tsv to csv format
filename = input("Enter filename:")
infile = open(filename)
# Get the output filename
outfilename = input("Enter output filename:")
# This is how you might automatically create the output filename
# outfilename = filename[:-3] + "csv"
outfile = open(outfilename,"w")
# Loop over the file and replace the tabs on each line with commas
for line in infile:
    line = line.strip()
    line = line.replace("\t",",")
    outfile.write(line + "\n")
outfile.close()
