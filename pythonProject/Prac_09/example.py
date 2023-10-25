# Exercise 4
def question_4():
    try:
        with open("name.txt", "r") as in_file:
            name = in_file.read().strip()
            print(f"Greetings {name}!")
    except FileNotFoundError:
        print("The file 'name.txt' does not exist.")


# Exercise 5
def count_values_above_threshold(filename, threshold):
    count = 0
    total_values = 0
    with open(filename, "r") as in_file:
        for line in in_file:
            try:
                value = float(line.strip())
                total_values += 1
                if value > threshold:
                    count += 1
            except ValueError:
                pass
    return count, total_values


def question_5():
    filename = input("Enter the filename: ")
    threshold = float(input("Enter the threshold value: "))
    try:
        count, total_values = count_values_above_threshold(filename, threshold)
        print(f"Filename: {filename}")
        print(f"Threshold: {threshold}")
        print("Processing...")
        print(
            f"{count} out of {total_values} ({(count / total_values) * 100:.1f}%) values in {filename} are greater than {threshold}.")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except ValueError:
        print("Invalid threshold value. Please enter a valid number.")


# Exercise 6
def filter_file(input_filename, output_filename, search_string):
    with open(input_filename, "r") as in_file, open(output_filename, "w") as out_file:
        for line in in_file:
            if search_string in line:
                out_file.write(line)


def question_6():
    input_filename = input("Enter the input filename: ")
    output_filename = input("Enter the output filename: ")
    search_string = input("Enter the search string: ")

    try:
        filter_file(input_filename, output_filename, search_string)
        print(f"Filtered data written to '{output_filename}'.")
    except FileNotFoundError:
        print(f"The file '{input_filename}' does not exist.")


if __name__ == "__main__":
    question_4()
    question_5()
    question_6()
