# Question 1: Processing Strings
def question_1():
    data_strings = ["Result = 95%", "Final Score = 8%", "Relative Value = 178%",
                    "Something else that's very important = 9.2%", "x = 42%"]

    for data in data_strings:
        equals_index = data.index("=")
        percent_index = data.index("%")
        value = data[equals_index + 2:percent_index]
        print(float(value))  # Convert the extracted value to a float and print it

# Question 2: Date Strings
def question_2():
    dob = input("Enter your date of birth (DD/MM/YYYY): ")
    year_of_birth = dob[-4:]  # Extract the last 4 characters (the year)
    current_year = 2022  # Update this to the current year when you run the program
    age = current_year - int(year_of_birth)
    print(f"You were born in {year_of_birth}.")
    print(f"You will turn {age + 1} in {current_year + 1}.")

# Question 3: Subject Code Strings
def question_3():
    while True:
        subject_code = input("Enter a subject code (or leave blank to exit): ")
        if not subject_code:
            break  # Exit the loop if the user leaves the input blank
        discipline = subject_code[:2]
        year_level = int(subject_code[2])
        it_subject = "IT" if discipline == "CP" else "Masters or other" if discipline == "CP" else "non-IT"
        year_string = "first-year" if year_level == 1 else "second-year" if year_level == 2 else "third-year"
        print(f"That is a {year_string} {it_subject} subject.")

# Main program
if __name__ == "__main__":
    question_1()
    question_2()
    question_3()
