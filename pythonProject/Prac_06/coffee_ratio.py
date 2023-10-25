import random

def calculate_ratio(dose, yield):
    return yield / dose

def determine_coffee_style(ratio):
    if ratio < 1:
        return "ristretto"
    elif 1 <= ratio < 2:
        return "normale"
    elif 2 <= ratio < 3:
        return "lungo"
    else:
        return "lungo"

def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number

def main():
    dose = get_valid_number("Dose (g): ", 0, 100)
    yield_amount = get_valid_number("Yield (g): ", 0, 100)
    ratio = calculate_ratio(dose, yield_amount)
    style = determine_coffee_style(ratio)
    print(f"{dose}:{yield_amount} is considered {style}")

if __name__ == "__main__":
    main()
