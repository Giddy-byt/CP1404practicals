# Get user's steak choice and convert it to lowercase
choice = input("Steak choice (rare, medium, or well-done): ").lower()

# Initialize the cooking time variable
cooking_time = 0

# Determine cooking time based on the user's choice
if choice == "rare":
    cooking_time = 5
elif choice == "medium":
    cooking_time = 7
elif choice == "well-done":
    cooking_time = 10
elif choice == "burnt":
    cooking_time = 8
else:
    print("Invalid choice. Please choose from rare, medium, well-done, or burnt.")
    exit()

# Print the estimated cooking time
print(f"Steak will be cooked {choice} and will take {cooking_time} minutes.")
