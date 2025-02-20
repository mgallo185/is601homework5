from app.commands import CommandHandler
from app.commands.add_command import AddCommand
from app.commands.subtract_command import SubtractCommand
from app.commands.multiply_command import MultiplyCommand
from app.commands.divide_command import DivideCommand
from app.commands.menu_command import MenuCommand 
class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.command_handler.register_command("add", AddCommand())  # Register instance
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))
    def start(self):
        print("Welcome to Calculator, type 'menu' to see available commands")
        self.command_handler.execute_command("menu")
        while True:
            user_input = input("Enter command: ")
            if user_input.lower() == "exit":
                break
            self.command_handler.execute_command(*user_input.split())  # Pass split input
