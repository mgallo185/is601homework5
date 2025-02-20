from decimal import Decimal, InvalidOperation
from app.calculation import Calculator
from app.commands import Command

class DivideCommand(Command):
    def __init__(self):
        super().__init__()
    
    def execute(self, *args):
        if len(args) != 2:
            print("Usage: divide <number1> <number2>")
            return
        
        try:
            num1, num2 = map(Decimal, args)
            if num2 == 0:
                print("Error: Division by zero is not allowed")
                return
            result = Calculator.divide(num1, num2)
            print(f"Result: {num1} ÷ {num2} = {result}")
        except InvalidOperation:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"Error: {e}")
