"""
Stronk module
"""

import secrets as random
import os


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
SYMBOLS = '!@#$%+=?&*()'


def generate_random_keys(number_of_keys=1, key_length=16, identify=False):
    """ Returns the generated keys """
    number_of_keys_iterator = 0
    keys = []
    error_message = ''
    if number_of_keys > 100:
        error_message += "ERROR: Number of keys must be <= 100\n"
    if number_of_keys <= 0:
        error_message += "ERROR: Number of keys must be non-zero and non-negative\n"
    if key_length > 256:
        error_message += "ERROR: Key length must be <= 256\n"
    if key_length < 16:
        error_message += "ERROR: Key length must be non-zero and non-negative\n"
    if not error_message:
        while number_of_keys_iterator < number_of_keys:
            key_length_iterator = 0
            key = ''
            while key_length_iterator < key_length:
                key += str(_generate_random_char())
                key_length_iterator += 1
            keys.append(_shuffle_key(key))
            number_of_keys_iterator += 1
        _prettify_output(keys, identify)
        _print_to_txt_file(keys, identify)
        return keys
    _prettify_output(error_message, False)
    return error_message


def generate_sha5_hash():
    """ Generate sha5 hash """
    return 0


def _shuffle_key(key):
    """ Returns the shuffled key """
    random.SystemRandom().shuffle(list(key))
    return ''.join(key)


def _generate_random_char():
    """ Generate a random integer, letter, or symbol """
    character_type = random.randbelow(13)
    if character_type == (0 or 1 or 2):
        return random.randbelow(10)
    if character_type == (3 or 4):
        return random.choice(SYMBOLS)
    return random.choice(LETTERS)


def _prettify_output(output, identify):
    if isinstance(output, list):
        for iterator, out in enumerate(output):
            if identify:
                print("(" + str(iterator + 1) + ") " + out)
            else:
                print(out)
    else:
        print(output)


def _print_to_txt_file(keys, identify):
    current_working_directory = os.getcwd()
    output_file = open(current_working_directory + "/stronk.txt", "w")
    for iterator, key in enumerate(keys):
        if identify:
            output_file.write("(" + str(iterator + 1) + ") " + key + "\n")
        else:
            output_file.write(key + "\n")

    output_file.close()
