def addition_calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print("The result of addition is:", result)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    addition_calculator()
