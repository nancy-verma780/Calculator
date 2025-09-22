def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def Power(x, y):
    return x ** y

def divide(x, y):
    if y == 0:
        return "Not Defined"
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulo")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice not in ['1','2','3','4','5','6']:
        print("Invalid please try again.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input.")
        return

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    elif choice == '5':
        result = num1 ** num2
    elif choice == '6':
        if num2 == 0:
            result = "Syntax Error"
        else:
            result = num1 % num2

    print(f"Result: {result}")

def main():
    while True:
        calculator()
        again = input("Do you want to perform another calculation? (y/n): ").lower()
        if again != 'yes':
            print("Thanks!")
            break

if __name__ == "__main__":
    main()

