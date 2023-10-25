import random

# List of valid coffee orders
coffee_menu = ["Flat White", "Espresso", "Long Black", "Babyccino", "Cappuccino"]

# Coffee making functions
def grind_beans():
    print("- Insert portafilter into grinder")
    print("- Press grind button to grind beans into portafilter")

def distribute_grounds():
    print("- Distribute grounds")

def tamp_grounds():
    print("- Tamp grounds")

def insert_portafilter():
    print("- Insert full portafilter into group head")

def pour_espresso():
    print("- Press shot button to pour espresso into cup")

def add_hot_water():
    print("- Add hot water to cup")

def make_coffee(coffee_choice):
    print(f"Here's how to make a/n {coffee_choice}:")
    grind_beans()
    distribute_grounds()
    tamp_grounds()
    insert_portafilter()
    pour_espresso()
    if coffee_choice == "Long Black":
        add_hot_water()

def main():
    print("Welcome to the IT@JCU Coffee Shop")
    while True:
        print("(O)rder - (D)rink - (R)andom choice - (Q)uit")
        choice = input(">>> ").strip().lower()
        if choice == "o":
            order_coffee()
        elif choice == "d":
            drink_coffee()
        elif choice == "r":
            random_choice()
        elif choice == "q":
            print("Thanks for drinking coffee")
            break
        else:
            print("Invalid option")

def order_coffee():
    print("Please choose from: ")
    for coffee in coffee_menu:
        print(coffee)
    order = input("Enter your coffee order: ").strip().title()
    if order in coffee_menu:
        make_coffee(order)
    else:
        print("Invalid order")

def drink_coffee():
    print("Mmmm, nice choice!")

def random_choice():
    coffee_choice = random.choice(coffee_menu)
    make_coffee(coffee_choice)
    print(f"Randomly selected: {coffee_choice}")

if __name__ == "__main__":
    main()
