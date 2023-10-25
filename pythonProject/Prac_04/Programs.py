# 1. Error Checking
MIN_WORKER_LEVEL = 1
MAX_WORKER_LEVEL = 10

worker_level = int(input("Worker level: "))
while worker_level < MIN_WORKER_LEVEL or worker_level > MAX_WORKER_LEVEL:
    print("Invalid worker level")
    worker_level = int(input("Worker level: "))

salary = worker_level * 5000
print(f"With worker level {worker_level}, your salary is ${salary:,.2f}")

# 2. Number Sequences
# a.
for i in range(1, 100, 2):
    print(i)

# b.
current_year = 2023
while current_year >= 1896:
    print(current_year, end=' ')
    current_year -= 4

print()  # Print a newline

# c. You can choose any meaningful sequence, here's one for even numbers from 2 to 20.
for i in range(2, 21, 2):
    print(i, end=' ')

# 3. Menus
choice = ""
while choice.lower() != 'q':
    print("(S)miley")
    print("(F)rowny")
    print("(Q)uit")
    choice = input("Choose an option: ").lower()
    if choice == 's':
        print(":-)")
    elif choice == 'f':
        print(":(")
    elif choice != 'q':
        print("Invalid choice")
print("Farewell")

# 4. Accumulation - Average Age
SENTINEL = -1
total_age = 0
num_people = 0

while True:
    age = int(input("Enter the age of a person (or -1 to quit): "))
    if age == SENTINEL:
        break
    total_age += age
    num_people += 1

if num_people > 0:
    average_age = total_age / num_people
    print(f"The average age of {num_people} people is {average_age:.2f}")
else:
    print("No ages entered.")

# 4. Accumulation - Smileys Count
smiley_count = 0
frowny_count = 0

while True:
    choice = input("Enter 'S' for smiley, 'F' for frowny, or 'Q' to quit: ").upper()

    if choice == 'Q':
        break
    elif choice == 'S':
        smiley_count += 1
    elif choice == 'F':
        frowny_count += 1
    else:
        print("Invalid choice. Please enter 'S', 'F', or 'Q'.")

print(f"You printed {smiley_count} smileys and {frowny_count} frownies.")

#Total numbers
total = 0

num_repetitions = int(input("How many numbers do you want to add up? "))

for i in range(num_repetitions):
    number = float(input(f"Enter number {i + 1}: "))
    total += number

print(f"The total of those {num_repetitions} numbers is {total:.2f}")
# I used definite iteration because we know how many times the loop will run based on the
#user's input. This allows us to use a 'for' loop with a specified range of repetitions.

# 5. Guessing Game
import random

MIN_SECRET = 1
MAX_SECRET = 100
SECRET = random.randint(MIN_SECRET, MAX_SECRET)
guess = -1
guess_count = 0

while guess != SECRET:
    guess = int(input("Guess a number: "))
    guess_count += 1
    if guess < SECRET:
        print("Higher")
    elif guess > SECRET:
        print("Lower")

print(f"You got it in {guess_count} guesses!")

# 6. Nested Loops
rows = int(input("Rows: "))
columns = int(input("Columns: "))

for i in range(rows):
    for j in range(columns):
        print(j, end=' ')
    print()  # Print a newline
