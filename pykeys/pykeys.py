"""
Pykeys module
"""

import secrets as random


key = ''
keys = []
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
symbols = '!@#$%+=?&*()'
character_type = 1


def generate_random_keys(number_of_keys=1, key_length=16):
    """ Returns the generated keys """
    number_of_keys_iterator = 0
    keys = []
    while number_of_keys_iterator < number_of_keys:
        key_length_iterator = 0
        key = ''
        while key_length_iterator < key_length:
            key += str(_generate_random_char())
            key_length_iterator += 1
        keys.append(_shuffle_key(key))
        number_of_keys_iterator += 1
    return keys


def generate_sha5_hash():
    """ Generate sha5 hash """
    return self


def _shuffle_key(key):
    """ Returns the shuffled key """
    random.SystemRandom().shuffle(list(key))
    return ''.join(key)


def _generate_random_char():
    """ Generate a random integer, letter, or symbol """
    character_type = random.randbelow(3)
    if character_type == 0:
        return random.randbelow(10)
    if character_type == 1:
        return random.randbelow(len(letters))
    if character_type == 2:
        return random.randbelow(len(symbols))
