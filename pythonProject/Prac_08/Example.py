places = []
place = input("Place: ")
while place != "":
 places.append(place)
 place = input("Place: ")
print("On my holiday, I went to: ")
for place in places:
 print(place)