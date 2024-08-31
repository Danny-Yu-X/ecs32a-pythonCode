places = ["MU", "Silo", "Latitudes", "Segundo"]
print(places)
print(places[0])

places.append("Segundo") # adds to a list
places.pop() # removes from a list

places_to_eat = []
for day in range(7):
    places_to_eat.append(random.choice(places))
#

menu = []
menu_item = ["Bagel", 3.25]
menu.append(menu_item)
menu


menu_item = ["Muffin", 4.15]
menu.append(menu_item)
menu_item

menu[1][1]

#

for i in range(len(places_to_eat)):
    places_to_eat[i] = str(i+1) + " " +places_to_eat[i]


#
