import argparse

# Define parser instance
parser = argparse.ArgumentParser()

# Add positional arguments
parser.add_argument("name", help="Input your name")

# Add optional arguments
parser.add_argument("-a", "--age", help="Input your age", type=int)

# Parse arguments
args = parser.parse_args()

# Print arguments
print(args)
print(args.name)
print(args.age)
