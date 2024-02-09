"""
This module is used for interfacing with Clipstar through the command line.


"""


def execute_help(subject=""):
    """Prints information about Clipstar's modules or commands."""
    print(f"help {subject}")


def execute_options(module=""):
    """Allows alteration of Clipstar's options."""
    print(f"options {module}")


def execute_clear():
    """Clears all the history in the console."""
    print("clear")


def execute_exit():
    """Exits Clipstar."""
    print("exit")


commands = {
    "help": execute_help,
    "options": execute_options,
    "clear": execute_clear,
    "exit": execute_exit,
}
