# __main__.py

import sys

from stronk import stronk


def output_helper(keys):
    stronk._prettify_output(keys)
    stronk._print_to_txt_file(keys)


def main():
    """ Spit out a string regardless of input """
    if len(sys.argv) == 2:
        output_helper(stronk.generate_random_keys(int(sys.argv[1]), 16))
    elif len(sys.argv) >= 3:
        output_helper(stronk.generate_random_keys(
            int(sys.argv[1]), int(sys.argv[2])))
    else:
        output_helper(stronk.generate_random_keys())


if __name__ == "__main__":
    main()
