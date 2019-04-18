# __main__.py
import sys
import argparse

from stronk import stronk


def getArguments():
    """ Parses CLI arguments """
    parser = argparse.ArgumentParser(description='Generate strong keys.')
    parser.add_argument('keyAmount', metavar='K', type=int, nargs='?', const='1', default='1',
                        help='number of keys to generate')
    parser.add_argument('keyLength', metavar='L', type=int, nargs='?', const='16', default='16',
                        help='number of keys to generate')
    parser.add_argument('--identify', '-i', action='store_true', required=False,
                        help='print the keys with a number beside them')
    return parser


def main():
    """ Spit out a string regardless of input """
    args = getArguments().parse_args()
    if len(sys.argv) == 2:
        stronk.generate_random_keys(
            args.keyAmount, args.keyLength)
    elif len(sys.argv) >= 3:
        stronk.generate_random_keys(
            args.keyAmount, args.keyLength, args.identify)
    else:
        stronk.generate_random_keys()


if __name__ == "__main__":
    main()
