     #1. Tax

        #Decision Pattern
    #We use the if, elif, and else decision pattern to determine the tax category based on the income:

    #If income is less than the low threshold, total_tax is set to 0 (no tax).
    #If income is between the low and high thresholds, we calculate tax based on the low tax rate.
    #If income is above the high threshold, we calculate tax based on the high tax rate.

TAX_RATE_LOW = 0.05  # 5%
TAX_RATE_HIGH = 0.1  # 10%
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_HIGH = 1000

print("Python Party Tax Program - Where Tax is a Party")
income = float(input("Income: $"))

# Determine the tax category based on income
if income < TAX_THRESHOLD_LOW:
    total_tax = 0
elif income <= TAX_THRESHOLD_HIGH:
    total_tax = income * TAX_RATE_LOW
else:
    total_tax = income * TAX_RATE_HIGH

# Calculate take-home pay
take_home_pay = income - total_tax

print("Total tax is: $", total_tax, sep="")
print("Take home pay is: $", take_home_pay, sep="")


    #2. Car Insurance

      #Decision pattern
#We take user input for the applicant's age using input and convert it to an integer using int().
#We use the if, elif, and else decision pattern to check the age in a specific order:
#If the age is less than 18, we output "Hire refused" because applicants under 18 are refused hire altogether.
#If the age is less than 25 (but not less than 18, thanks to the previous condition), we output "Insurance required" because applicants under 25 are required to purchase special insurance.
#If none of the above conditions are met, we output "Insurance not required" because applicants 25 years and over are notrequired to purchase insurance.

print("Painz Car Rental - Insurance Check")
age = int(input("Enter your age: "))

if age < 18:
    print("Hire refused")
elif age < 25:
    print("Insurance required")
else:
    print("Insurance not required")

        #3. Simple Password checker
    #Design Pattern
#define a constant SECRET_PASSWORD to store the secret password.
#We use input to get the user's input for their password and store it in the variable user_password.
#We use a string comparison with == to check if user_password matches the SECRET_PASSWORD.
#If the passwords match, we print "Access granted."
#If the passwords do not match, we print "Access denied."

# Constant for the secret password
SECRET_PASSWORD = "mysecretpassword"

# Get the user's input for the password
user_password = input("Enter the password: ")

# Check if the user's password matches the secret password
if user_password == SECRET_PASSWORD:
    print("Access granted")
else:
    print("Access denied")

        #4. Dog Years
    #Design Pattern
#first get the user's age in human years using input and convert it to an integer.
#check if the age is valid (between 0 and 120 inclusive) using a compound Boolean expression.
#If the age is valid, we calculate the age in dog years based on the provided formula.
#then print the age in both human and dog years.
#Additionally, we provide custom responses based on different age categories using if-elif-else statements.
#If the age is invalid, we print "Invalid age."

    # Get the user's age in human years
    age_in_human_years = int(input("Enter your age in human years: "))

    # Check if the age is valid (between 0 and 120 inclusive)
    if 0 <= age_in_human_years <= 120:
        # Calculate the age in dog years
        if age_in_human_years <= 2:
            age_in_dog_years = age_in_human_years * 10.5
        else:
            age_in_dog_years = 2 * 10.5 + (age_in_human_years - 2) * 4

        # Print the age in human years and dog years
        print("Age in human years:", age_in_human_years)
        print("Age in dog years is", age_in_dog_years)

        # Custom responses based on age
        if age_in_human_years <= 12:
            print("You're still young!")
        elif age_in_human_years <= 18:
            print("You're a teenager now.")
        elif age_in_human_years <= 30:
            print("Enjoy your twenties!")
        else:
            print("You have a lot of life experiences.")
    else:
        print("Invalid age")

        #5. Rock of ages

        #Design Patttern
#first get the user's age using input and convert it to an integer.
#check if the age is valid (between 0 and 120 inclusive) using a single compound Boolean expression.
#If the age is valid, we provide custom responses based on different age categories using if-elif-else statements.
#If the age is invalid, we print "Invalid age."

# Get the user's age
age = int(input("Enter your age: "))

# Check if the age is valid (between 0 and 120 inclusive)
if 0 <= age <= 120:
    # Custom responses based on age categories
    if age < 18:
        print("You are a minor.")
    elif age < 30:
        print("You are a young adult.")
    elif age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
else:
    print("Invalid age")

        #6. Speeding Fines
    #Design Patterns
#get the user's speed and the speed limit as input.
#calculate the speed over the limit once and store it in the speed_over_limit variable.
#use a single if-elif-else structure to determine the fine amount based on the speed over the limit.
#format the fine amount as a currency with two decimal places using an f-string.

# Get user's speed and speed limit
speed = float(input("Enter your speed (km/h): "))
speed_limit = float(input("Enter the speed limit (km/h): "))

# Calculate the speed over the limit
speed_over_limit = speed - speed_limit

# Check the speeding conditions and calculate the fine
if speed_over_limit < 11:
    fine = 309
elif speed_over_limit <= 20:
    fine = 464
elif speed_over_limit <= 30:
    fine = 696
elif speed_over_limit <= 40:
    fine = 1161
else:
    fine = 1780

# Display the fine amount
print(f"Your fine amount is ${fine:.2f}")
