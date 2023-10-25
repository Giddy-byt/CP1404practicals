def calculate_grade(score):
    if score < 50:
        return "F"
    elif 50 <= score < 65:
        return "P"
    elif 65 <= score < 75:
        return "C"
    elif 75 <= score < 85:
        return "D"
    else:
        return "HD"

def main():
    while True:
        score = float(input("Enter your subject total score (negative value to exit): "))
        if score < 0:
            break
        grade = calculate_grade(score)
        print(f"The score {score} is {grade}")

if __name__ == "__main__":
    main()
