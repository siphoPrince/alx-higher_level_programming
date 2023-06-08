#!/usr/bin/python3
import sys

def print_arguments():
    argument_count = len(sys.argv) - 1

    if argument_count == 0:
        print("No arguments provided.")
    elif argument_count == 1:
        print("Argument:")
    else:
        print("Number of arguments: {}".format(argument_count))

for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}. {}".format(i, arg))

if __name__ == "__main__":
    print_arguments()
