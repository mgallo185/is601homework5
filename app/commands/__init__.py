from abc import ABC, abstractmethod
class Command(ABC):
    """Abstract base class for commands."""
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    """Handles command registration and execution."""
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        """Registers a command with a name."""
        self.commands[command_name] = command

    def execute_command(self, command_name: str, *args):
        """Executes a registered command if it exists."""
        try:
            self.commands[command_name].execute(*args)
        except KeyError:
            print(f"No such command: {command_name}")
        except TypeError:
            print(f"Invalid arguments for command: {command_name}")
            
    def get_registered_commands(self):
        """Returns a list of registered command names."""
        return list(self.commands.keys())