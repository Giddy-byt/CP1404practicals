def calculate_grade(score):
    if 0 <= score < 50:
        return "N"
    elif 50 <= score < 65:
        return "P"
    elif 65 <= score < 75:
        return "C"
    elif 75 <= score < 85:
        return "D"
    elif 85 <= score <= 100:
        return "HD"
    else:
        return "Invalid"


def main():
    num_scores = 4
    scores = []

    for i in range(num_scores):
        score = float(input(f"Score {i + 1}: "))
        scores.append(score)

    total_score = sum(scores)
    average_score = total_score / num_scores

    print("\nGrade for each score:")
    for i, score in enumerate(scores):
        grade = calculate_grade(score)
        print(f"Score {i + 1} was {score:.1f}, which is {grade}")

    print(f"The average score was {average_score:.3f}")

    trend = "positive" if scores[-1] > average_score else "not positive"
    print(f"The trend is {trend}")


if __name__ == "__main__":
    main()
