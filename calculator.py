def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error! Division by zero is not allowed."
    return num1 / num2

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operation (+ for addition, - for subtraction, * for multiplication, / for division): ")

        if operator == '+':
            result = addition(num1, num2)
        elif operator == '-':
            result = subtraction(num1, num2)
        elif operator == '*':
            result = multiplication(num1, num2)
        elif operator == '/':
            result = division(num1, num2)
        else:
            result = "Invalid operator! Please enter +, -, *, or /."

        print("The result is:", result)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
