def calculate_dog_years(human_years):
    if human_years <= 2:
        return human_years * 10.5
    else:
        return 21 + 4 * (human_years - 2)

def main():
    while True:
        human_years = float(input("Enter an age in human years (negative number to quit): "))
        if human_years < 0:
            print("Goodbye!")
            break
        dog_years = calculate_dog_years(human_years)
        print(f"{human_years} human years is {dog_years} dog years")

if __name__ == "__main__":
    main()
