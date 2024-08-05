"""
Shows how to use argparse to create command-line applications
"""

import argparse
import pprint


def main() -> int:
    # ==========================================
    # ======== Define Parser Instance ==========
    # ==========================================
    parser = argparse.ArgumentParser()

    """
    ADD POSITIONAL ARGUMENTS
    - Positional arguments are required
    - Use help="description" to add a description of the argument
    """
    parser.add_argument("name", help="Input your name")

    """
    ADD OPTIONAL ARGUMENTS
    - Use single-dash (short option)
    - Use double-dash (long option)
    - Specify additional options as a default
    - Use "default=VALUE" to set a default value if argument is not provided
    - Use "required=True" to make argument required
    """
    parser.add_argument(
        "-c",  # short option
        "--config",  # long option
        "--config-file",  # alias
        default="config.json",  # Specify default
        # required=True,  # Make optional argument required
        help="Specify the config file. (default: %(default)s)",
    )

    """
    SPECIFY TYPES
    - Use type=TYPE to specify type of argument
    - If argument's value is a valid type, it will be converted to that type
    - If argument's value is not a valid type, it will raise an error
    """
    parser.add_argument(
        "--days",
        type=int,
    )

    """
    ADD BOOLEAN OPTIONS
    - action="store_true": Set argument's value to True (option is False by default)
    - action="store_false": Set argument's value to False (option is True by default)
    """
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
    )

    """
    CONSTRAIN VALUES TO SPECIFIED CHOICES
    Specify Choices with choices=("VALUE", "VALUE", ...)
    If argument's value is not in choices, it will raise an error
    """
    parser.add_argument("--color", choices=("auto", "always", "never"), default="auto")

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
