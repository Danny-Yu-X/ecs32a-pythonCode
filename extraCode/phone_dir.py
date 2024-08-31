# phone_dir.py
# ECS32A
#
# Read in a phone directory
# and filter entries based on area code

def main():
    # Read in an index of area codes to states
    area_codes_to_state = read_state_data()
    # read in a phone directory and filter it by state
    filter_phone_dir('California', area_codes_to_state)
    

# read_state_data reads in an index of area codes to states
def read_state_data():
    # Create new empty dictionary
    ac_to_state = {}
    infile = open("areaCodes.csv")
    for line in infile:
        # remove whitespace
        line = line.strip()
        # split this file on comma 
        codes = line.split(",")
        # the first element in this list will be the state
        # remove it and add it to the variable state
        state = codes.pop(0)
        # dictionary maps area codes to states
        for code in codes:
            ac_to_state[code] = state
    return ac_to_state

# filter_phone_dir takes a state and a dictionary
# mapping area codes to states. it reads the phone
# directory file 'phoneDir.txt' and prints only
# those phone numbers with area codes belonging to
# the parameter state
def filter_phone_dir(state, ac_to_state):
    infile = open("phoneDir.txt","r")
    for line in infile:
        line = line.strip()
        # unpack phone directory entry into name and phone number
        name,phone = line.split("\t")
        # get the area code
        area_code = phone[1:4]
        # look up the state given the area code
        # one area code, 999, is bad and will not
        # be found in the dictionary so we should
        # protect against crashing by checking first
        if area_code in ac_to_state:
            lookup_state = ac_to_state[area_code]
        else:
            # Go to next line of the phone directory
            # if you cannot look up the state for an
            # area code
            continue 

        # Print phone number only if from state (California)
        if lookup_state == state:
            print(name, phone, state)
        
        
    
main()
