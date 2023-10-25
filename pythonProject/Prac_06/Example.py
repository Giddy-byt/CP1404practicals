# Function to calculate BMI
def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)


# Function to determine weight category
def determine_weight_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# Main program
def main():
    print("BMI Calculator")
    weight_kg = float(input("Enter your weight in kilograms: "))
    height_m = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight_kg, height_m)
    weight_category = determine_weight_category(bmi)

    print(f"Your BMI is {bmi:.2f}")
    print(f"You are categorized as '{weight_category}'")


if __name__ == "__main__":
    main()
