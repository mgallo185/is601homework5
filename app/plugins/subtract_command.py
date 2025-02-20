from decimal import Decimal, InvalidOperation
from app.calculation import Calculator
from app.commands import Command

class SubtractCommand(Command):
    def __init__(self):
        super().__init__()
    
    def execute(self, *args):
        if len(args) != 2:
            print("Usage: subtract <number1> <number2>")
            return
        
        try:
            num1, num2 = map(Decimal, args)
            result = Calculator.subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        except InvalidOperation:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"Error: {e}")
