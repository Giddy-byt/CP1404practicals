def main():
    record = ["Jimmy", "Smith", (8, 12, 1928), "piano"]

    # Extract and print specific data
    last_name = record[1]
    born = record[2]
    birth_year = born[2]
    instrument = record[3]

    print(f"Last name: {last_name}")
    print(f"Born: {born}")
    print(f"{record[0]} was born in {birth_year} and was a great {instrument} player.")


if __name__ == "__main__":
    main()
