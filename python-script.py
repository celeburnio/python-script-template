#!/usr/bin/python3

"""
    Script template
"""

__author__ = 'Your name'
__email__ = 'your@email.com'
__version__ = '0.0.0'

# Imports
import argparse
import sys

# Global variables

# Functions

def parse_arguments():
    """ Returns de parsed args """
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description='Script description')
    parser.add_argument('--example', '-e', help='An argument example', type=str)
    parser.add_argument('--flagexample', '-f', help='Flag argument example', action='store_true')
    return parser.parse_args()

def main():
    """ main """
    # Parse arguments
    args = parse_arguments()
    if args.example:
        print('The argument example introduced is: ' + args.example)

    if args.flagexample:
        print('The flag is true')
    sys.exit(0)
if __name__ == '__main__':
    main()
