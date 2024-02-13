"""
This module is the main entry point of Clipstar.

Initialises the application, sets up necessary configurations,
and begins the command line interfacing.
"""

import sys


def exit_clipstar(is_cursor_inline=False):
    """Prints an exit message then exits Clipstar."""
    if is_cursor_inline:
        print()

    print("Exiting...")
    sys.exit()


def main():
    """Main entry point of Clipstar."""
    try:
        while True:
            input("Clipstar> ")

    except KeyboardInterrupt:
        exit_clipstar(is_cursor_inline=True)


if __name__ == "__main__":
    main()
