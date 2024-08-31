
def read_gdp_data(happy_dict):
    #opens world_pop_gdp.tsv for reading
    infile = open("world_pop_gdp.tsv")
    happy_index = None
    #loops for each line in the file, stripping whitespace, replacing $ and ,
    # for "", splitting each line by the tab and assinging variables to each
    #element and outputs the country name, population in mil, and GDP per cap
    #loops until the last line of the file
    for line in infile:
        #strip off whitespace character
        line = line.strip()
        #remove "$" sign
        line = line.replace("$", "")
        #remove ","
        line = line.replace(",", "")
        #split on the tab and assign each element with variables country
        #popoulation and gdp
        country, population, gdp, happy_index = line.split("\t")
        if country in happy_dict:
            happy_index = happy_dict[country]
            print(country + "," + population + "," + gdp + "," + happy_index)
    return
