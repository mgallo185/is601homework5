from decimal import Decimal, InvalidOperation
from app.calculation import Calculator
from app.commands import Command

from decimal import Decimal, InvalidOperation
from app.calculation import Calculator
from app.commands import Command

class MultiplyCommand(Command):
    def execute(self, *args):
        if len(args) != 2:  # Ensure exactly two arguments
            print("Usage: multiply <number1> <number2>")
            return

        try:
            num1, num2 = map(Decimal, args)  # Convert input to decimals
            result = Calculator.multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        except InvalidOperation:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"Error: {e}")
