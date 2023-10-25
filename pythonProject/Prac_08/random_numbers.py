import random


def main():
    num_numbers = int(input("How many random numbers: "))
    max_number = int(input("Maximum number: "))

    numbers = [random.randint(0, max_number) for _ in range(num_numbers)]

    print(f"The numbers are: {numbers}")
    print(f"The minimum is {min(numbers)}")
    print(f"The maximum is {max(numbers)}")

    random_choice = random.choice(numbers)
    print(f"A randomly chosen number is {random_choice}")

    numbers.reverse()
    print(f"The numbers reversed are {numbers}")

    numbers.sort()
    print(f"The numbers sorted are {numbers}")


if __name__ == "__main__":
    main()
