#Calculate salary for worker level(with functions)
MIN_WORKER_LEVEL = 1
MAX_WORKER_LEVEL = 10


def get_valid_worker_level():
    while True:
        worker_level = int(input("Worker level: "))
        if MIN_WORKER_LEVEL <= worker_level <= MAX_WORKER_LEVEL:
            return worker_level
        else:
            print("Invalid worker level")


def calculate_salary(worker_level):
    return worker_level * 5000


def main():
    print("Calculate Salary based on Worker Level")

    worker_level = get_valid_worker_level()
    salary = calculate_salary(worker_level)

    print(f"With worker level {worker_level}, your salary is ${salary:,.2f}")


if __name__ == "__main__":
    main()

#Print grid(rows, columns)
def generate_multiplication_table(rows, columns):
    table = [[i * j for j in range(1, columns + 1)] for i in range(1, rows + 1)]
    return table

def print_multiplication_table(table):
    for row in table:
        for num in row:
            print("{:4}".format(num), end=" ")
        print()

def main():
    rows = 15
    columns = 15

    multiplication_table = generate_multiplication_table(rows, columns)
    print_multiplication_table(multiplication_table)

if __name__ == "__main__":
    main()

