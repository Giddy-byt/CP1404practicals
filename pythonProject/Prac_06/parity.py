def print_parity(num):
    parity = num % 2
    print(f"Parity of {num} should be {parity}: {parity}")


def calculate_parity(num):
    return num % 2


def is_odd(num):
    return num % 2 == 1


def main():
    num1 = 4
    num2 = 41
    print_parity(num1)
    print_parity(num2)

    num3 = 7
    num4 = 12
    print(f"Is {num3} odd? {is_odd(num3)}")
    print(f"Is {num4} odd? {is_odd(num4)}")


if __name__ == "__main__":
    main()
