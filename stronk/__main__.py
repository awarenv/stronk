# __main__.py
import sys

from stronk import stronk


def main():
    """ Spit out a string regardless of input """
    if len(sys.argv) == 2:
        stronk.generate_random_keys(int(sys.argv[1]), 16)
    elif len(sys.argv) >= 3:
        stronk.generate_random_keys(
            int(sys.argv[1]), int(sys.argv[2]))
    else:
        stronk.generate_random_keys()


if __name__ == "__main__":
    main()
