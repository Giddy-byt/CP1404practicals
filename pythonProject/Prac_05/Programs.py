

# 1. Percentage change
original = float(input("Original: "))
change = float(input("Change: "))
result = original + (original * change)
print(f"Original: {original}, Change: {change}, Result: {result}")

# 2. Time of day
time = int(input("Time of day (0-23 hours): "))
coming_or_going = input("Are you coming or going? ").lower()
daytime = "before noon" if time < 12 else "after noon"
greeting = "Hi!" if coming_or_going == "coming" else "Bye!"
print(f"It is {daytime} and you are {coming_or_going}. {greeting}")

# 3. Coffee orders
coffee_type = input("White or black coffee: ").lower()
coffee_size = input("Choose size (small, medium, or large): ").lower()
black_prices = {"small": 3, "medium": 4, "large": 5}
white_prices = {"small": 4, "medium": 5, "large": 6}
price = white_prices[coffee_size] if coffee_type == "white" else black_prices.get(coffee_size, 6)
print(f"Cost: ${price:.2f}")

# 4. Coffee orders with error-checking
coffee_type = input("White or black coffee: ").lower()
coffee_size = input("Choose size (small, medium, or large): ").lower()
while coffee_type not in ["white", "black"] or coffee_size not in ["small", "medium", "large"]:
    coffee_type = input("Invalid input. White or black coffee: ").lower()
    coffee_size = input("Invalid input. Choose size (small, medium, or large): ").lower()
price = white_prices[coffee_size] if coffee_type == "white" else black_prices[coffee_size]
print(f"Cost: ${price:.2f}")

# 5. Accumulation
low_value = int(input("Enter a low value: "))
high_value = int(input("Enter a high value: "))
total = 0
for num in range(low_value, high_value + 1):
    total += num
print(*range(low_value, high_value + 1), f"totals: {total}")

