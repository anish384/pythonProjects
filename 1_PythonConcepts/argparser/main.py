import argparse

# parser = argparse.ArgumentParser()
# parser.parse_args()

# if i run this it will give below error

"""
:!python3 main.py foo
:!python3 main.py foo

usage: main.py [-h]
main.py: error: unrecognized arguments: foo

shell returned 2
"""

# parser = argparse.ArgumentParser()
# parser.add_argument("echo")
# args = parser.parse_args()
# print(args.echo)

# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display square of given number", type=int)
#
# args = parser.parse_args()
# print(args.square ** 2)

""" Optional Argument """
"""
    here we need to give `--verbosity 1` then verbosity is set to true
"""
# parser = argparse.ArgumentParser()
# parser.add_argument("--verbosity", help="added verbosity")
# args = parser.parse_args()
# if(args.verbosity):
#     print("verbosity turned on")

"""
    here we need to give `--verbose` then verbosity is set to true
    if i give `--verbose 1` then it will say unrecognized argument 
"""
# parser = argparse.ArgumentParser()
# parser.add_argument("--verbose", "-v", help="added verbosity", action="store_true")
# args = parser.parse_args()
#
# if(args.verbose):
#     print("verbosity turned on")

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="returns square")
parser.add_argument("--verbose", help="gives a verbose output", action="store_true")

args = parser.parse_args()
if(args.verbose):
    print(f"square of {args.square} is {args.square ** 2}")
else:
    print(f"{args.square ** 2}")
