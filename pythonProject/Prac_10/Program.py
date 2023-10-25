# Question 1
def print_line():
    print("-" * 40)

def question_1():
    print_line()

# Question 2
def is_even(number):
    return number % 2 == 0

def question_2():
    some_number = int(input("Number: "))
    if is_even(some_number):
        print(f"{some_number} is even")
    else:
        print(f"{some_number} is odd")

# Question 3
def get_non_empty_string(prompt):
    while True:
        user_input = input(prompt)
        if user_input != "":
            return user_input
        else:
            print("Input cannot be blank")

def question_3():
    name = get_non_empty_string("Enter your name: ")
    birthplace = get_non_empty_string("Enter your birthplace: ")
    print(f"Hi {name} from {birthplace}!")

# Question 4
def generate_number_list(minimum, maximum):
    return list(range(minimum, maximum + 1))

def question_4():
    while True:
        try:
            minimum = int(input("Minimum number: "))
            maximum = int(input("Maximum number: "))
            if maximum <= minimum:
                print("Your maximum must be greater than the minimum")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    numbers = generate_number_list(minimum, maximum)
    print(numbers)

# Question 5
def is_valid_subject(subject):
    if len(subject) == 6 and subject[:2].isalpha() and subject[2:].isdigit():
        return True
    else:
        return False

def question_5():
    subjects = []
    while True:
        subject = input("Enter subject code: ").upper()
        if subject == "":
            break
        if is_valid_subject(subject):
            subjects.append(subject)

    subjects.sort()
    print("\nYou do these", len(subjects), "subjects:")
    for subject in subjects:
        print(subject)

    if "CP1401" in subjects:
        print("You are cool")
    else:
        print("You are not cool")

if __name__ == "__main__":
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()
