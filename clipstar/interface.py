"""
This module is used for interfacing with Clipstar through the command line.


"""

def execute_help(subject):
    """Prints usage to the console."""
    print(f"help {subject}")

commands = {
    "help": execute_help
}
