# dog.py
# Danny Yu
# The program prompts the user to enter a weather condition and outputs instructions for walking their dog based on their entered weather.
# If the user says that weather is sunny, the program then prompts the user for the temperature and outputs instructions for walking their dog based on the temperature.

#prompts the user to enter a weather condition
weather = input("Enter weather condition (rainy/sunny/snowy/cloudy):") # keeps track of the weather
# checks to see if the user entered rainy as the weather
if weather == "rainy":
    #outputs the walkiing instructions based on rainy weather
    print("Instructions for the walk:")
    print("The dog should be taken for a short walk with an umbrella.")
#checks to see if the user entered sunny as the weather
elif weather == "sunny":
    #prompts the user to enter temperature in degrees fahrenheit
    temperature = int(input("Enter temperature:")) # keeps track of the temperature
    # checks to see if the temperature is greater than 80 and less than or equal to 114
    if temperature > 80 and temperature <= 114:
    #outputs the walking instructions based on sunny weather and in the given temperature range
        print("Instructions for the walk:")
        print("The dog should be taken for a walk in the shade and given water.")
    #checks to see if the temperature is greater than 45 and less than or equal to 80
    elif temperature > 45 and temperature <= 80:
        #outputs the walking instructions based on sunny weather and in the given temperature range
        print("Instructions for the walk:")
        print("The dog can enjoy a regular walk.")
    #checks to see if the temperature is greater than -14 and less than or equal to 45
    elif temperature > -14 and temperature <= 45:
        #outputs the walking instructions based on sunny weather and in the given temperature range
        print("Instructions for the walk:")
        print("Dress the dog warmly for a walk.")
    # checks to see if the temperature is greater than 114 degrees
    elif temperature > 114:
        print("Instructions for the walk:")
        print("Invalid weather condition.")
# checks to see if the user entered snowy as the weather
elif weather == "snowy":
    #outputs the walking instructions based on snowy weather
    print("Instructions for the walk:")
    print("Take the dog for a short walk and ensure they stay warm.")
# checks to see if the user entered cloudy as the weather
elif weather == "cloudy":
    #outputs the walking instructions based on cloudy weather
    print("Instructions for the walk:")
    print("Enjoy a regular walk with your dog.")
# checks to ese if the user entered a weather condition other than rainy, sunny, snowy, or cloudy
else:
    print("Instructions for the walk:")
    print("Invalid weather condition.")
