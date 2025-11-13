from scientific import square_root, logarithm, factorial, sin_function, cos_function


# Enhanced Basic Calculator Operations (from Developer A)
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero!"
    return a % b


# Menu System (from Developer C)
def display_main_menu():
    print("\n" + "=" * 40)
    print("        ENHANCED CALCULATOR")
    print("=" * 40)
    print("1. Basic Operations")
    print("2. Scientific Operations")
    print("3. Exit")
    print("=" * 40)

    choice = input("Enter your choice (1-3): ")
    return choice


def basic_operations():
    while True:
        print("\n--- Basic Operations ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Modulus")
        print("7. Back to Main Menu")

        choice = input("Enter operation choice (1-7): ")

        if choice == '7':
            return

        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = add(num1, num2)
                    print(f"Result: {num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"Result: {num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"Result: {num1} × {num2} = {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"Result: {num1} ÷ {num2} = {result}")
                elif choice == '5':
                    result = power(num1, num2)
                    print(f"Result: {num1} ^ {num2} = {result}")
                elif choice == '6':
                    result = modulus(num1, num2)
                    print(f"Result: {num1} % {num2} = {result}")

                # Wait for user to continue
                input("\nPress Enter to continue...")

            except ValueError:
                print("Error: Please enter valid numbers!")
                input("Press Enter to continue...")
        else:
            print("Invalid choice! Please try again.")


def scientific_operations():
    while True:
        print("\n--- Scientific Operations ---")
        print("1. Square Root")
        print("2. Logarithm")
        print("3. Factorial")
        print("4. Sine")
        print("5. Cosine")
        print("6. Back to Main Menu")

        choice = input("Enter operation choice (1-6): ")

        if choice == '6':
            return

        try:
            if choice == '1':
                num = float(input("Enter number: "))
                result = square_root(num)
                print(f"Result: √{num} = {result}")
            elif choice == '2':
                num = float(input("Enter number: "))
                result = logarithm(num)
                print(f"Result: log({num}) = {result}")
            elif choice == '3':
                num = float(input("Enter number: "))
                result = factorial(num)
                print(f"Result: {num}! = {result}")
            elif choice == '4':
                degrees = float(input("Enter angle in degrees: "))
                result = sin_function(degrees)
                print(f"Result: sin({degrees}°) = {result}")
            elif choice == '5':
                degrees = float(input("Enter angle in degrees: "))
                result = cos_function(degrees)
                print(f"Result: cos({degrees}°) = {result}")
            else:
                print("Invalid choice! Please try again.")

            # Wait for user to continue
            input("\nPress Enter to continue...")

        except ValueError:
            print("Error: Please enter valid numbers!")
            input("Press Enter to continue...")


def main():
    print("Welcome to the Enhanced Calculator!")
    print("This calculator combines basic and scientific operations.")

    while True:
        choice = display_main_menu()

        if choice == '1':
            basic_operations()
        elif choice == '2':
            scientific_operations()
        elif choice == '3':
            print("\nThank you for using the Enhanced Calculator! Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()