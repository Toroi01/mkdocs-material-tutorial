import argparse
from .greetings import Greeter


def main():
    """
    The main entry point for the greeting program.

    This function sets up a command-line interface (CLI) to accept the user's
    name as input, creates a Greeter instance, generates a greeting, and prints it.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(description="A simple greeting program.")
    parser.add_argument("name", help="The name of the person to greet")
    args = parser.parse_args()

    # Create a Greeter instance and generate greeting
    greeter = Greeter(args.name)
    greeting = greeter.greet()
    print(greeting)


if __name__ == "__main__":
    main()
