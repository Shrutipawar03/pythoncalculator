def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
    print("Options:")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.Exit")

    user_input = input(": ")

    if user_input == "quit":
        break

    if user_input in ("1","2","3","4","5"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "1":
            print("Result:", add(num1, num2))
        elif user_input == "2":
            print("Result:", subtract(num1, num2))
        elif user_input == "3":
            print("Result:", multiply(num1, num2))
        elif user_input == "4":
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")
