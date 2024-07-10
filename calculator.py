def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def main():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == '1':
                    result = add(num1, num2)
                    print(f"The result of {num1} + {num2} is {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"The result of {num1} - {num2} is {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"The result of {num1} * {num2} is {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"The result of {num1} / {num2} is {result}")

            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == '5':
            print(" Thank You...Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
