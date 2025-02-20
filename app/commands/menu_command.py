from app.commands import Command

class MenuCommand(Command):
    def __init__(self, command_handler):
        """Initialize with reference to CommandHandler to access registered commands."""
        self.command_handler = command_handler

    def execute(self, *args):
        """Display available commands."""
        print("\nAvailable Commands:")
        for command_name in self.command_handler.get_registered_commands():
            print(f"  🔹 {command_name}")
        print("Type 'exit' to quit.\n")
