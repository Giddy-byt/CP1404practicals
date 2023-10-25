# Question 4: Read a String from a File
def question_4():
    try:
        with open("name.txt", "r") as in_file:
            name = in_file.read().strip()
            print(f"Greetings {name}!")
    except FileNotFoundError:
        print("File not found. Please create a file named 'name.txt' with your name in it.")

# Question 5: Greater-Than Counter
def question_5():
    filename = input("Enter the filename: ")
    threshold = float(input("Enter the threshold value: "))
    try:
        with open(filename, "r") as in_file:
            lines = in_file.readlines()
            total_lines = len(lines)
            count = sum(1 for line in lines if float(line) > threshold)
            percentage = (count / total_lines) * 100
            print(f"Filename: {filename}")
            print(f"Threshold: {threshold}")
            print("Processing...")
            print(f"{count} out of {total_lines} ({percentage:.1f}%) values in {filename} are greater than {threshold}.")
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please make sure the file exists.")

# Question 6: File Filter
def question_6():
    input_filename = input("Enter the input filename: ")
    output_filename = input("Enter the output filename: ")
    search_string = input("Enter the search string: ")
    try:
        with open(input_filename, "r") as in_file, open(output_filename, "w") as out_file:
            for line in in_file:
                if search_string in line:
                    out_file.write(line)
    except FileNotFoundError:
        print(f"Input file '{input_filename}' not found. Please make sure the file exists.")
