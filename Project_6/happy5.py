# happy5.py
# Danny Yu
# This program opens the happiness.csv file for reading and outputs each
# country and happiness index through a created function make_happy_dict()
#The make_happy_dict() function's return value of a created dictionary is assigned
#to happy_dict, the variable defined in main.
#The program then passes the happy_dict as an argument to read_gdp_data()
# and reads the input file world_pop_gdp.tsv file and outputs each
#country name, population in millions, and the GDP per capita contained
#in that file
#The program also includes happiness index part of the output by checking
#if the country found in world_pop_gdp.tsv is a key in happy_dict


#this main function for part 1 assigns the return value dictionary made in
#make_happy_dict() to happy_dict
def main():

    # Part 1
    # Build dictionary mapping countries to happiness index
    #assign the return value of happy_dictionary in make_happy_dict() to happy_dict
    happy_dict = make_happy_dict()
    

    # Part 2
    # Print key value pairs sorted by key
    # Uncomment the function call below for part 2 only
    # call to print_sorted_dictionary for output of the key value pairs
    #print_sorted_dictionary(happy_dict)

    # Part 3
    # Uncomment the function call below for part 3 only
    # lookup happiness by country until the user enters done
    #pass the happy_dict as an argument for the function to output the
    #happiness index when a country is input by the user
    #lookup_happiness_by_country(happy_dict)

    # Parts 4-6
    # Uncomment the function call below for parts 4-6 
    # Read file containing population and GDP data and add happiness data
    # output each country, population in mil, and GDP per capita, and Happiness
    read_gdp_data(happy_dict)


#this function opens happiness.csv file for reading and adds each
#key value pairs of country and happiness index on each line to an
#empty dictionary
#this function also outputs the country and happiness index
#The function returns a dictionary containing keys of countries and values of
#happyiness indexes contained in happiness.csv
def make_happy_dict():
    #opens the happiness.csv file for reading
    infile = open("happiness.csv")
    #ignores the header of the file
    infile.readline()
    #create empty dictionary
    happy_dictionary = {}
    #loops for each line in the file, stripping whitespace, assigning variables
    #to each comma separated value and adds each country as a key and happiness
    #index as a value to the empty dictionary
    #loops until the last line of the file
    for line in infile:
        #strips off whitespace characters (\n)
        line = line.strip()
        #split the values by the comma and assign them to variables
        country, year, happy_index = line.split(",")
        #adds each country as a key and each happiness index as a
        #corresponding value to the empty dictionary
        happy_dictionary[country] = happy_index
        #outputs the country and corresponding happiness index
        #print(country, happy_index)
        #returns the new dictionary that has key value pairs of country
        #and corresponding happiness index
    return happy_dictionary

#This function reads world_pop_gdp.tsv file and loops
#for each line, printing out each country name, population in mil, and GDP,
# per captia
#This function also checks if the country in world_pop_gdp.tsv is a key
#in the happy_dict dictionary and also includes the happiness index in the comma
#separated output
def read_gdp_data(happy_dict):
    #opens world_pop_gdp.tsv for reading
    infile = open("world_pop_gdp.tsv")
    #make local variable a None type to not have unboundlocalerror
    happy_index = None
    print("Country,Population in Millions,GDP per Capita,Happiness")
    #loops for each line in the file, stripping whitespace, replacing $ and ,
    # for "", splitting each line by the tab and assinging variables to each
    #element and outputs the country name, population in mil, and GDP per cap
    #loops until the last line of the file
    #also includes happiness index associated with the country if the country
    #is a key in happy_dict
    for line in infile:
        #strip off whitespace character
        line = line.strip()
        #remove "$" sign
        line = line.replace("$", "")
        #remove ","
        line = line.replace(",", "")
        #split on the tab and assign each element with variables country
        #popoulation and gdp
        country, population, gdp = line.split("\t")
        #checks if the country from world_pop_gdp.tsv is a key in happy_dict
        if country in happy_dict:
            #keeps track of the happiness values assosicated with the
            #key country
            happy_index = happy_dict[country]
    #outputs country, population in millions, Gdp per capita, and happiness
            print(country + "," + population + "," + gdp + "," + happy_index)
    return


#this function loops through input from the user and if the user inputs a
#key country that is in the dictionary, the corresponding happiness index
#value is outputted. 
def lookup_happiness_by_country(happy_dict):
    #indefinite while loop that loops for user input and outputs the
    #corresponding happiness index if the input is a key in the dictionary
    #loops until "done" is input 
    while True:
        #prompts the user to input a country name
        country = input("Enter a country to lookup or 'done' to exit:")
        #checks that the user inputs "done" and breaks out the loop
        if country == "done":
            break
        #checks if the user input is a key in the dictionary
        if country in happy_dict:
            #outputs the corresponding happiness index value
            print(happy_dict[country])
        #checks that user input is not a key in the dictionary
        else:
            print(country, "not found")
    return

# Function prints all the values in a dictionary d sorted by key
# returns "Dictionary not found" if the type of the parameter is not a dictionary
def print_sorted_dictionary(D):
    #checks if the type of the argument passed to the parameter is not a dictionary
    if type(D) != type({}):
        print("Dictionary not found")
        return
    print("Contents of dictionary sorted by key.")
    print("Key","Value")
    #loops for each key in the dictionary and sorts them
    #loops until the last key
    for key in sorted(D.keys()):
        #outputs the key value pair of the country and happiness index
        print(key, D[key])
#call to main function        
main()
