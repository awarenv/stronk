# __main__.py

import sys

from pykeys import pykeys

def output_helper(keys):
  pykeys._prettify_output(keys)
  pykeys._print_to_txt_file(keys)

def main():
  """ Spit out a string regardless of input """
  if len(sys.argv) == 2:
    output_helper(pykeys.generate_random_keys(int(sys.argv[1]), 16))
  elif len(sys.argv) >= 3:
    output_helper(pykeys.generate_random_keys(
        int(sys.argv[1]), int(sys.argv[2])))
  else:
    output_helper(pykeys.generate_random_keys(1, 16))

if __name__ == "__main__":
    main()
