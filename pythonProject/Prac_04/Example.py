MINIMUM_MONTH = 1
MAXIMUM_MONTH = 12

birth_month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))

while birth_month < MINIMUM_MONTH or birth_month > MAXIMUM_MONTH:
    print("Invalid month")
    birth_month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))

if birth_month <= 6:
    print("You were born in the first half of the year.")
else:
    print("You were born in the second half of the year.")
