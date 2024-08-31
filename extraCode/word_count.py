# word_count.py
# 
# Count the number of unique words in a file
def main():
    # open a user specified file
    infile = open_user_file()
    # read file and make list
    lines = file_to_lines(infile)
    # split list
    words = split_lines(lines)
    #make word count dictionary
    word_counts = make_word_count_dict(words)
    print("Unique words:", len(word_counts))
    #print("Total words:", )
    
    # make unique list
    #uniq_words = unique(words)
    # get_count_for_query 
    #get_count_for_query(words)


#make_word_count_dict(words)
#Create a dictionary of words in the text mapping to their counts
def make_word_count_dict(words):
    word_counts = {}
    for word in words:
##        if word in word_counts:
##            word_counts[word] = word_counts[word] + 1
##        else:
##            word_counts[word] = 1
##        return word_counts
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts
        
                

make_word_count_dict(words)



# get_count_for_query asks the user for query words
# and will get the counts for them
def get_count_for_query(words):
    while True:
        query = input("Enter query word or return to exit:")
        if query == "":
            break
        count = words.count(query)
        print(query, count)
    return

# open_user_file asks the user for a filename
# and opens it for reading returning the open
# filehandle
def open_user_file():
    while True:
        filename = input("Enter filename:")
        try:
            infile = open(filename)
            break
        except:
            print("File",filename,"not found")
            continue
    return infile

# file_to_lines reads a filehandle
# and returns a list of the lines of
# text in the file as strings
def file_to_lines(infile):
    # list of lines from the file
    lines = []
    # loop though the lines of the file
    for line in infile:
        line = line.strip()
        lines.append(line)
    return lines

# split_lines converts a list of lines to words by
# splitting each line on whitespace characters
def split_lines(lines):
    words = []
    for line in lines:
        line_words = line.split()
        for word in line_words:
            words.append(word)  
    return words

# unique takes a list of potentially duplicated items
# and creates a new list where every item appears only
# once. E.g. ['one','one','two'] becomes ['one','two']
def unique(words):
    uniq_words = []
    for word in words:
        if word not in uniq_words:
            uniq_words.append(word)
    return uniq_words

main()

