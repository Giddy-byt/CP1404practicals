#Algorithm with IPO (Input, Processing, Output):
# Input
dose = float(input("Enter the dose (in grams): "))
yield_ = float(input("Enter the yield (in grams): "))

# Processing
brew_ratio = dose / yield_

# Output
print(f"The brew ratio is {brew_ratio:.2f}")

#Algorithm with Decision:

# input
item_price = float(input("Enter the price of the item: "))
money_in_pocket = float(input("Enter the money you have in your pocket: "))

# Decision
if item_price <= money_in_pocket:
    print("You can afford to buy the item.")
else:
    print("You cannot afford to buy the item.")

    #Algorithm with Repetition:

# Algorithm with Repetition
print("Start cleaning the room.")
while True:
    things_on_floor = int(input("Enter the number of things on the floor: "))
    if things_on_floor == 0:
        break
    print(f"Pick up one thing from the floor. {things_on_floor - 1} things left.")
print("End cleaning.")



