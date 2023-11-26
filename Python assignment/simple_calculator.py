class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Error: Cannot divide by zero.")
        return num1 / num2

def get_user_input():
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        return num1, operator, num2
    except ValueError:
        raise ValueError("Error: Non-numeric input for numbers.")

def perform_calculation(calculator, num1, operator, num2):
    try:
        if operator == '+':
            result = calculator.add(num1, num2)
        elif operator == '-':
            result = calculator.subtract(num1, num2)
        elif operator == '*':
            result = calculator.multiply(num1, num2)
        elif operator == '/':
            result = calculator.divide(num1, num2)
        else:
            raise ValueError("Error: Invalid operator input.")
        return result
    except Exception as e:
        raise ValueError(f"Error: {str(e)}")

def main():
    calculator = Calculator()

    try:
        num1, operator, num2 = get_user_input()
        result = perform_calculation(calculator, num1, operator, num2)
        print(f"Result: {result}")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
