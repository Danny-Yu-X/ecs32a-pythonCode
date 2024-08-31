# write_song.py

outfile = open("song.txt", "w")

line = "I'm a lumjack and I'm OK"
print(line)
outfile.write(line)
line = "I work all night and I sleep all day"
print(line)
outfile.write(line + "\n")

outfile.close()
