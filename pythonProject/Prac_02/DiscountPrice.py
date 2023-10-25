# 1. Discount Price
original_price = float(input("Enter the original price: $"))
DISCOUNT_RATE = 0.2  # Constant for discount rate (20%)
discount = original_price * DISCOUNT_RATE
new_price = original_price - discount
print("The discounted price is $", new_price, sep="")
