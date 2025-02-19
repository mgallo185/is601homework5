from app.commands import CommandHandler
from app.commands.add_command import AddCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.command_handler.register_command("add", AddCommand())  # Register instance

    def start(self):
        while True:
            user_input = input("Enter command: ")
            if user_input.lower() == "exit":
                break
            self.command_handler.execute_command(*user_input.split())  # Pass split input
