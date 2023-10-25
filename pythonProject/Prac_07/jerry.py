def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt + ": "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def convert_miles_to_km(speed_in_mph):
    return speed_in_mph * 1.60934

def determine_fine(speed_in_km, speed_limit_in_kph):
    if speed_in_km <= speed_limit_in_kph:
        return 0
    elif speed_in_km <= speed_limit_in_kph + 10:
        return 50
    elif speed_in_km <= speed_limit_in_kph + 20:
        return 100
    else:
        return 200

def main():
    speed_in_mph = get_valid_number("Enter your speed in mph")
    speed_limit_in_kph = get_valid_number("Enter the speed limit in kph")
    speed_in_kph = convert_miles_to_km(speed_in_mph)
    fine = determine_fine(speed_in_kph, speed_limit_in_kph)
    print(f"Your fine is ${fine:.2f}")

if __name__ == "__main__":
    main()
