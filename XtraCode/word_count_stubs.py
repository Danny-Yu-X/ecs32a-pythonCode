# word_count.py
# EDIT CODE ERRORS ALRT LOL
# Count the number of unique words in a file
def main():
    # open a user specified file
    infile = open_user_file()
    # read file and make list
    lines = file_to_lines(infile)
    # split list
    words = split_lines(lines)
    # make unique list
    uniq_words = unique(words)
    #get count for query
    get_count_for_query()

#get_count_for_query asks the user for query words
def get_count_for_query():

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
            print("File", filename, "not found.")
            continue
    return infile

# file_to_lines reads a filehandle
# and returns a list of the lines of
# text in the file as strings
def file_to_lines(infile):
    lines = []
    #loop through the lines of the file
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

