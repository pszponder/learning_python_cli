import argparse
import time

# ==========================================
# ======== Define Parser Instance ==========
# ==========================================
parser = argparse.ArgumentParser()

# ==========================================
# ======== Add Positional Arguments ========
# ==========================================
# # These arguments are required
# parser.add_argument("x", type=int, help="First number")
# parser.add_argument("y", type=int, help="Second number")

# ==========================================
# ========= Add Optional Arguments =========
# ==========================================
parser.add_argument(
    "-v", "--verbose", type=int, choices=[0, 1, 2], default=0, help="Verbosity level"
)

# # pass in up to 2 numbers as arguments (nargs="2")
# parser.add_argument(
#     "-n", "--numbers", type=float, nargs=2, help="The numbers to be added"
# )

# pass in as many numbers as you want (nargs="*")
parser.add_argument(
    "-n", "--numbers", type=float, nargs="*", help="The numbers to be added"
)

# Add a boolean flag for enabling debugging
# If specified, it will be set to True, otherwise False
parser.add_argument("-d", "--debug", action="store_true", help="Enable debugging")


# ==========================================
# ============= Parse Arguments ============
# ==========================================
args = parser.parse_args()

# ==========================================
# =========== Use Parsed Arguments =========
# ==========================================
if args.debug:
    print("Debugging is enabled...")
    start = time.perf_counter()

if args.verbose is None or args.verbose == 0:
    print("Verbosity level is 0")
    if args.numbers is not None:
        # print(args.numbers[0] + args.numbers[1]) # For case where nargs="2"
        print(f"Sum of Numbers: {sum(args.numbers)}")  # For case where nargs="*"
elif args.verbose == 1:
    print("Verbosity level is 1")
    if args.numbers is not None:
        # print(args.numbers[0] + args.numbers[1]) # For case where nargs="2"
        print(f"Sum of Numbers: {sum(args.numbers)}")  # For case where nargs="*"
else:
    print("Verbosity level is 2")
    if args.numbers is not None:
        print(f"Numbers to Add: {args.numbers}")
        # print(args.numbers[0] + args.numbers[1]) # For case where nargs="2"
        print(f"Sum of Numbers: {sum(args.numbers)}")  # For case where nargs="*"

if args.debug:
    print("Debugging is enabled...")
    end = time.perf_counter()
    print("Elapsed Time: ", end - start)
