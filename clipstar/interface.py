"""
This module is used for interfacing with Clipstar through the command line.


"""

def execute_help(subject = ""):
    """Prints information about Clipstar's modules or commands."""
    print(f"help {subject}")

def execute_options(module = ""):
    """Allows alteration of Clipstar's options."""
    print(f"options {module}")

commands = {
    "help": execute_help,
    "options": execute_options,
}
