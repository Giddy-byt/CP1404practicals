#Program 1:
#Problems:

# 'number' is not being passed as an argument to the calculate_parity function.
# 'number % 2' does not calculate the parity as intended.

    #Fixed code:

def main_1():
    """Determine the parity of a user's number."""
    number = int(input("Enter number: "))
    parity = calculate_parity(number)  # Pass 'number' as an argument to calculate_parity
    print(parity)

def calculate_parity(number):
    """Calculate the parity (0 or 1) of number passed in."""
    return number % 2  # Correct the parity calculation

#Program 2:
#Problem(s):

# 'numnums' should be converted to an integer.
#The loop is iterating over characters in 'numnums', not numbers.
#Multiplying a character by 2 does not produce the desired output.

    #Fixed code:

def main_2():
    """Print numbers from 0 up to the user's input multiplied by 2."""
    numnums = int(input("How many: "))  # Convert 'numnums' to an integer
    for i in range(numnums):  # Iterate using 'range' for numbers
        print(i * 2)

#Program 3:
#Problem(s):

#The function 'calculate_area' prints the result instead of returning it.
#The 'length' and 'width' variables should be taken as user inputs, not predefined values.

    #Fixed code:

def main_3():
    """Determine the area of a rectangle."""
    length = float(input("Length: "))  # Prompt user for length and width
    width = float(input("Width: "))
    area = calculate_area(length, width)
    print(f"The area is {area:.2f}")

def calculate_area(l, w):
    """Calculate the area of a rectangle from its dimensions."""
    result = l * w
    return result  # Return the calculated area

#Program 4:
#Problem(s):

#The while condition should use the logical OR ('or') operator, not 'and'.
#The age check is incorrect; it should be if age is less than 0 or greater than 120.

    #Fixed code:

def main_4():
    """Show how old a person will be in the future."""
    increment = 10
    age = int(input("Age: "))
    while age < 0 or age > 120:  # Use 'or' instead of 'and' in the condition
        print("Invalid age")
        age = int(input("Age: "))
    print(f"In {increment} years, you will be {age + increment} years old!")  # Correct age calculation
