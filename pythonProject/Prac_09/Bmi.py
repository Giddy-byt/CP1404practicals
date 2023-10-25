def question_7():
    def calculate_bmi(height, weight):
        return weight / (height ** 2)

    def get_weight_category(bmi):
        if bmi < 18.5:
            return "underweight"
        elif 18.5 <= bmi < 25.0:
            return "normal"
        elif 25.0 <= bmi < 30.0:
            return "overweight"
        else:
            return "obese"

    num_people = int(input("Enter the number of people: "))
    try:
        with open("bmis.txt", "w") as out_file:
            for _ in range(num_people):
                height = float(input("Enter height (in meters): "))
                weight = float(input("Enter weight (in kilograms): "))
                bmi = calculate_bmi(height, weight)
                weight_category = get_weight_category(bmi)
                out_file.write(f"{bmi:.1f}\n")

        print("BMI values written to 'bmis.txt'.")

        with open("bmis.txt", "r") as in_file:
            print("BMI values:")
            for line in in_file:
                bmi = float(line)
                category = get_weight_category(bmi)
                print(f"BMI {bmi:.1f}, considered {category}")

    except FileNotFoundError:
        print("File not found. Please make sure 'bmis.txt' exists.")

# Main program
if __name__ == "__main__":
    # Choose which question to run here
    question_4()
    question_5()
    question_6()
    question_7()