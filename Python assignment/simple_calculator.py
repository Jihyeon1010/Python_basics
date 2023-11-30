#produce the class that named Calculator
class Calculator:
    #define function add equal to num1 + num2
    def add(self, num1, num2):
        return num1 + num2
    #define function subtract equal to num1 - num2
    def subtract(self, num1, num2):
        return num1 - num2
    #define function multiply equal to num1 multiply num2
    def multiply(self, num1, num2):
        return num1 * num2
    #define function divide equal to num1 divide by num2 when it do not occur of error
    def divide(self, num1, num2):
        #if input value of num2 equal to 0, error is occur and print the error message 
        if num2 == 0:
            raise ValueError("Error: Cannot divide by zero.")
        return num1 / num2

#define the function get_user_input
def get_user_input():
    #valid circumstance
    try:
        #define variable: num1, data type is float and used input 
        num1 = float(input("Enter the first number: "))
        #define variable: operator and used input 
        operator = input("Enter the operator (+, -, *, /): ")
        #define num2, data type is float and receive the input via user
        num2 = float(input("Enter the second number: "))
        return num1, operator, num2
    #if write the invalid value such as non-numeric input value 
    except ValueError:
        raise ValueError("Error: Non-numeric input for numbers.")

#define function 
def perform_calculation(calculator, num1, operator, num2):
    #valid circumstance
    try:
        #if the input oprtator equal to "+"
        if operator == '+':
            #define the result equal to num1 + num2
            result = calculator.add(num1, num2)
        #if the input operator is -
        elif operator == '-':
            #define the result equal to num1 - num2 
            result = calculator.subtract(num1, num2)
        #if the input operator equal to *
        elif operator == '*':
            #define the result equal to num1 multiply num2
            result = calculator.multiply(num1, num2)
        #if the input operator equal to /
        elif operator == '/':
            #define the result equal to num1 divide by num2
            result = calculator.divide(num1, num2)
        #if input the invalid operator, print the error message
        else:
            raise ValueError("Error: Invalid operator input.")
        #export the result that depand on circumstance
        return result
    #if input value is invalid
    except Exception as e:
        raise ValueError(f"Error: {str(e)}")

def main():
    #define variable calculator equal to Class Calculator
    calculator = Calculator()
    #valid circumstance
    try:
        num1, operator, num2 = get_user_input()
        #define the result
        result = perform_calculation(calculator, num1, operator, num2)
        print(f"Result: {result}")
    #if the circumstance is invalid print error message
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
#define the python programming, which are able to produce to run the program
if __name__ == "__main__":
    main()