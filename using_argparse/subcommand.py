"""
Shows how to use argparse to create command-line applications
with subcommands
"""

import argparse
import pprint


def main() -> int:
    # ==========================================
    # ======== Define Parser Instance ==========
    # ==========================================
    parser = argparse.ArgumentParser()

    # ==========================================
    # ========= Create Subparsers ==============
    # ==========================================
    subparsers = parser.add_subparsers(dest="command", required=True)

    # ==========================================
    # ======== Add Subcommand 1 ================
    # ==========================================

    # Add a subparser called "add_parser"
    add_parser = subparsers.add_parser("add", help="Add two numbers")

    # Add arguments to "add_parser"
    add_parser.add_argument("x", type=int, help="First number")
    add_parser.add_argument("y", type=int, help="Second number")

    # ==========================================
    # ======== Add Subcommand 2 ================
    # ==========================================

    # Add a subparser called "subtract_parser"
    subtract_parser = subparsers.add_parser("subtract", help="Subtract two numbers")

    # Add arguments to "subtract_parser"
    subtract_parser.add_argument("x", type=int, help="First number")
    subtract_parser.add_argument("y", type=int, help="Second number")

    # ==========================================
    # ========= Parse Arguments ================
    # ==========================================
    args = parser.parse_args()

    # Print Arguments (args is converted from a Namespace object to a dictionary)
    pprint.pprint(vars(args))

    # Return exit code
    return 0


if __name__ == "__main__":
    exit(main())
