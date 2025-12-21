#get_col.py

filename = input("Enter input filename:")
infile= open(filename)
#determiine format
extension = filename[-3:].lower()

if extension == "csv":
    csv == True
else:
    csv == False


#get column to extract
col_num = int(input("Enter column number:"))

col_num = col_num - 1

outlines = []

for line in infile:
    line = line.strip()


    if csv == True
        cols = line.split(",")
#finish code here need another if statment of else
    cols = line.split("\t")
    col = cols[col_num]
    outlines.append(col)

#print(outlines)

filename = input("Enter output filename:")
outfile = open(filename, "w")

for line in outlines:
    outfile.write(line+ "\n")
    
outfile.close()
