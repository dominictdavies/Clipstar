"""
This module is used for interfacing with Clipstar through the command line.


"""

def execute_help(subject):
    """Prints usage to the console."""
    print(f"help {subject}")

def execute_options(module = ""):
    """Allows alteration of Clipstar's options."""
    print(f"options {module}")

commands = {
    "help": execute_help,
    "options": execute_options,
}
