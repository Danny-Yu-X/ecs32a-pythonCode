# phone_dir.py
# ECS32A
#
# Read in a phone directory
# add state based on area code
# and filter entries based on area code

def main():
    # Read in an index of area codes to states
    area_codes_to_state = read_state_data()
    #print(area_codes_to_state)
    # read in a phone directory and filter it by state
    filter_phone_dir(state, area_codes_to_state)
    

# read_state_data reads in an index of area codes to states
def read_state_data():
    return

# filter_phone_dir takes a state and a dictionary
# mapping area codes to states. it reads the phone
# directory file 'phoneDir.txt' and prints only
# those phone numbers with area codes belonging to
# the parameter state
def filter_phone_dir(filterState, ac_to_state):
    return
    
main()
