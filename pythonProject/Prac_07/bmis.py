def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)


def determine_weight_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 24.9:
        return "normal"
    elif bmi < 29.9:
        return "overweight"
    else:
        return "obese"


def main():
    heights = [1.5, 1.6, 1.7, 1.8, 1.9]
    weights = range(50, 101, 10)

    for height in heights:
        for weight in weights:
            bmi = calculate_bmi(weight, height)
            category = determine_weight_category(bmi)
            print(f"Height {height}m, Weight {weight}kg = BMI {bmi:.1f}, considered {category}")


if __name__ == "__main__":
    main()
