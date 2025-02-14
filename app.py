def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    """
    A simple calculator function that performs basic arithmetic operations.

    The user is prompted to select an operation from the following options:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Percentage

    The user is then prompted to enter two numbers, and the selected operation
    is performed on these numbers. The result is printed to the console.

    Functions:
    - add(a, b): Returns the sum of a and b.
    - subtract(a, b): Returns the difference of a and b.
    - multiply(a, b): Returns the product of a and b.
    - divide(a, b): Returns the quotient of a and b.

    Note:
    - If an invalid operation is selected, an "Invalid input" message is displayed.
    - Division by zero is not handled and will raise an error.
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")

    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

        elif choice == '5':
            print(f"{num1} % of {num2} = {multiply(num1, divide(num2, 100))}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()