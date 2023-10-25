def format_seconds(seconds):
    minutes, remaining_seconds = divmod(seconds, 60)
    return f"{minutes}m {remaining_seconds}s"


def main():
    for seconds in range(0, 3176, 635):
        print(f"{seconds} seconds is {format_seconds(seconds)}")

    favorite_seconds = int(input("Favourite duration in seconds: "))
    print(f"You love {format_seconds(favorite_seconds)}")


if __name__ == "__main__":
    main()
