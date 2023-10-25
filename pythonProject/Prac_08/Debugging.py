#Program 1 - Friends' Names:

names = ["Abby", "Jerome", "Olivia", "Monique"]
print("My friends' names: ")
for i in range(1, len(names)):
    print(f"{i}. {names[i]}")
last_number = len(names)
print(f"The last name (number {last_number}) is {names[last_number]}")

#Problems for Program 1:

#The loop starts from index 1, which means it will skip the first name ("Abby").
#It will attempt to access an index equal to the length of the list (names[last_number]),
# which is out of bounds. Python lists are zero-indexed.

#Fixed Code for Program 1:

names = ["Abby", "Jerome", "Olivia", "Monique"]
print("My friends' names: ")
for i in range(len(names)):  # Start the loop from 0
    print(f"{i + 1}. {names[i]}")  # Add 1 to i to display correct numbering

#Program 2 - Title-Casing Country Names:

countries = ("australia", "new zeaLAND", "India")
for i in range(len(countries)):
    countries[i] = countries[i].title()
print(countries)  # country names should be in title-case now

#Problems for Program 2:

#Tuple objects are immutable in Python, so you cannot modify individual elements of a tuple.
# This code will result in a TypeError.

#Fixed Code for Program 2:

countries = ("australia", "new zeaLAND", "India")
title_case_countries = tuple(country.title() for country in countries)
print(title_case_countries)  # country names should be in title-case now
