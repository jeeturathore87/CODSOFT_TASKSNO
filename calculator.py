def calculator():
    print("\n===== SIMPLE CALCULATOR =====")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        result = num1 + num2
        symbol = "+"
    elif choice == "2":
        result = num1 - num2
        symbol = "-"
    elif choice == "3":
        result = num1 * num2
        symbol = "*"
    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
        symbol = "/"
    else:
        print("Invalid choice!")
        return

    print(f"\nResult: {num1} {symbol} {num2} = {result}")


if __name__ == "__main__":
    calculator()
