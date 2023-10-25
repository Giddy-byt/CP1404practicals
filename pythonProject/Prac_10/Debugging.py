"""CP1401 - Practical 10 - Debugging.
Explain the problems (not the solution, not the style issues):
1. There are logical errors in the play function that prevent it from working as intended.
2. The code for calculating the result is incorrect.
3. The program doesn't check for valid input in the play function.
4. The variable names are not descriptive, making it hard to understand the code.
5. There's no handling for when the player goes bankrupt.

Describe your debugging process:
1. I ran the code and noticed that the program had logical errors, including incorrect calculations and lack of input validation.
2. I identified that the result calculation was not working as intended.
3. I noticed that there were issues with variable naming and readability.
4. I identified the need to check for valid input in the play function.
5. I observed that there was no handling for when the player goes bankrupt.

Fix the code in-place below
"""
import random

VALID_CHOICES = 'CA'
CONSERVATIVE_CHANCE = 40
CONSERVATIVE_REWARD = 1.5
AGGRESSIVE_CHANCE = 10
AGGRESSIVE_REWARD = 1.8


def main():
    money = 100
    print("Welcome to the gambling game!")
    print(f"You start with a balance of ${money}.")
    while money > 0:
        result = play(money)
        money += result
        print(f"Your new balance is ${money:.2f}")
        if money <= 0:
            print("You're out of money! Game over.")
    print("Thanks for playing :)")


def get_valid_amount(balance, amount):
    while amount < 0 or amount > balance:
        print("Invalid amount")
        amount = int(input("Enter amount to play: "))
    return amount


def play(balance):
    """Calculate and display whether win or lose based on chance."""
    amount = int(input("Enter amount to play: "))
    amount_to_risk = get_valid_amount(balance, amount)
    choice = 'x'
    while choice not in VALID_CHOICES:
        choice = input("(C)onservative, (A)ggressive: ").upper()
        if choice not in VALID_CHOICES:
            print("Invalid choice")
    risk_chance = random.randint(0, 101)
    if choice == "C" and risk_chance <= CONSERVATIVE_CHANCE:
        result = amount_to_risk * CONSERVATIVE_REWARD
        print(f"Congratulations! You earned ${result:.2f}")
    elif choice == "A" and risk_chance <= AGGRESSIVE_CHANCE:
        result = amount_to_risk * AGGRESSIVE_REWARD
        print(f"Congratulations! You earned ${result:.2f}")
    else:
        result = -amount_to_risk
        print(f"You lost ${amount_to_risk:.2f}")
    return result


main()

#ere are the changes made to the code:

#Corrected logical errors in the play function by adjusting the result calculations.
#Added input validation for the choice in the play function.
#Renamed variables to make the code more readable.
#Added handling for when the player goes bankrupt (money <= 0).