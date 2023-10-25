def calculate_price(num_products, price_per_product):
    if num_products < 0 or price_per_product <= 0:
        return None

    if num_products <= 5:
        total_price = num_products * price_per_product
    else:
        discounted_price = 0.9 * price_per_product  # 10% off
        total_price = num_products * discounted_price

    return total_price


def main():
    while True:
        print("Menu:")
        print("(I)nstructions")
        print("(C)alculate")
        print("(Q)uit")

        choice = input("Choice: ").upper()

        if choice == 'I':
            print("Enter the number of products you want to buy and your chosen price.")
            print("If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!")
        elif choice == 'C':
            num_products = int(input("Number of products: "))
            price_per_product = float(input("Price: "))

            total_price = calculate_price(num_products, price_per_product)

            if total_price is None:
                print("Invalid input")
            else:
                print(f"{num_products} x ${price_per_product:.2f} products = ${total_price:.2f}")
        elif choice == 'Q':
            print("Farewell")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
