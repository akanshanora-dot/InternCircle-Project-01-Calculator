
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a number.")


def calculator():
    print("\n--- Basic Calculator ---")
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("Choose operation (1-4): ")

        if choice == "1":
            print("Result:", a + b)
            break
        elif choice == "2":
            print("Result:", a - b)
            break
        elif choice == "3":
            print("Result:", a * b)
            break
        elif choice == "4":
            if b != 0:
                print("Result:", a / b)
            else:
                print("Cannot divide by zero!")
            break
        else:
            print("Invalid choice. Enter 1-4.")


def currency_converter():
    print("\n--- Currency Converter ---")
    print("Example rate: 1 USD = 83 INR")
    amount = get_number("Enter amount in USD: ")

    if amount < 0:
        print("Amount cannot be negative.")
        return

    print("Amount in INR:", round(amount * 83, 2))
    print("Note: Example exchange rate only.")


def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")

    while True:
        choice = input("Choose conversion (1-2): ")

        if choice in ("1", "2"):
            break

        print("Invalid choice. Enter 1 or 2.")

    value = get_number("Enter value: ")

    if choice == "1":
        print("Miles:", round(value * 0.621371, 4))
    else:
        print("Fahrenheit:", round((value * 9 / 5) + 32, 2))


while True:
    print("\n===== INTERACTIVE CALCULATOR =====")
    print("1. Calculator")
    print("2. Currency Converter")
    print("3. Unit Converter")
    print("4. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        calculator()
    elif option == "2":
        currency_converter()
    elif option == "3":
        unit_converter()
    elif option == "4":
        print("Thank you for using the program!")
        break
    else:
        print("Invalid choice. Enter 1-4.")
