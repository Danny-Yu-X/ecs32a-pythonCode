# ECS 32A
# Assignment 8
#counter3.py
# Danny Yu
# Writing a word counting class and making a wordle
#This program adds a key-value pair to the dictionary if the word is not
#already in the dictionary and increments its count by 1 if it already is in
#the dictionary. Returns and outputs the count for the specified words
#in the dictionary for that word and unique words.
# import wordle
import string

#
# The Count class
#
# The class keyword below begins the definition of a new Python data type Count.
# Count keeps word counts. All the methods that we can use with Count objects
# and the variables (attributes) built inside Count objects are defined in the
# this class definition.
#
class Count:
        #
        # Count constructor
        #
        # the __init__ method initializes the variables (attributes)
        # in Count objects, such as the dictionary datastructure that
        # hold the counts for each word. It is called when the count
        # object is first created using Count().
        #
        # The variable self refers to the object being initialized
        # So self.word_counts is referring to the word_count dictionay
        # within the object.
        #
        # Always add self in front of word_counts to access it within a method.
        def __init__(self):
            print("Word Counter Initialized")
                # Initialize word_counts to an empty dictionary
            self.word_counts = {}
                
        # The get_num_words method returns the number of words
        # (keys) in the word_counts dictionary.
        # This counts each word only once.
        def get_num_words(self):
                #returns the number of keys in the dictionary
            return len(self.word_counts) 

        # The increment_count method increments the count of a word. 
        # If word is not yet in the dictionary, self.word_counts,
        # it is added with a count of 1. If word is in the dictionary,
        # its count is incremented by 1.
        def increment_count(self,word):
                #checks if the word is not in the dictionary
            if word not in self.word_counts:
                    #adds the word as a key with value of 1
                self.word_counts[word] = 1
                #checks if the word is a key in the dict
            elif word in self.word_counts:
                    #increments the key's value by 1
                self.word_counts[word] = self.word_counts[word] + 1
                return

        # The lookup_count method returns the count of word
        # from the self.word_counts dictionary. If the word
        # is not in the dictionary, it returns 0.
        def lookup_count(self,word):
                #checks if word is in the dict
            if word in self.word_counts:
                    #returns the count of the word
                return self.word_counts[word]
                #checks if the word is not in the dict
            elif word not in self.word_counts:
                    #returns 0 for the count
                return 0

        # The get_top_words method gets the words with the highest
        # counts out of the dictionary.
        #
        # The parameter num indicates how many words to return.
        #
        # The method returns a list of num (count,word) tuples
        # sorted from higest to lowest.
        def get_top_words(self,num):
                return
        
# The main program 
def main():
                                
        ## Make a new Count object 
        ## the counter object will keep track of
        ## the counts for all the words in the book
        counter = Count()

        ## Test code for Part 3 and 4.
        ## Uncomment for Part 3 and 4.
        #counts the number of times Well occurs
        counter.increment_count("Well,")
        #counts the number of times oven occurs
        counter.increment_count("oven")
        #counts the number of times well occurs
        counter.increment_count("well")
        #counts the number of times .... occurs
        counter.increment_count("....'")
        #outputs the counts of the specified words
        print(counter.lookup_count("oven"))
        print(counter.lookup_count("well"))
        print(counter.lookup_count("pizza"))
        print(counter.lookup_count(""))

        ## For Part 5 Onward
        ## Open the user specified book file
        
##        filename = input("Enter book file:")
##        infile = open(filename)
        
        ## Put a loop here that extracts all words and
        ## inserts each word into the counter object by calling
        ## the counter.increment_count() method

        ## Test code for Part 5 and 6.
        ## Uncomment for Part 5 and 6.
        ## After completing Part 6 remove these lines
##        print("alice:",counter.lookup_count("alice"))
##        print("rabbit:",counter.lookup_count("rabbit"))
##        print("and:",counter.lookup_count("and"))
##        print("she:",counter.lookup_count("she"))
        ## Test code for Part 7. 
        ## Uncomment for Part 7.
##        print("Top 10 Words:")
##        top_ten = counter.get_top_words(10)
##        print(top_ten)

        #outputs the number of unique words

        print("Unique words:", counter.get_num_words())
        
        ## Finally, after you have submitted all parts
        ## of the assignment, uncomment the call to the
        ## wordle method below!
        ##
        ## You do not have to submit this part. 
        ##
        ## If there is a problem with your Tk installation
        ## the lab computers have been set up to run the code.
        ##
##        wordle.wordleFromObject(counter,30)

# Call the main program
main()
        
