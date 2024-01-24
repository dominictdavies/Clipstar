"""
This module is the main entry point of Clipstar.

Initialises the application, sets up necessary configurations,
and begins the command line interfacing.
"""

def string_recogniser(string):
    """Verifies if input is a string and appends a specific phrase to it."""
    if type(string) != str:
        raise TypeError()

    return string + " <- That's a string!"


def main():
    """Main entry point of Clipstar."""
    print("Hello world!")


if __name__ == "__main__":
    main()
