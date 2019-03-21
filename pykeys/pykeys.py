import secrets as random


def generate_random_ints(number_of_ints):
    int_subkey = ""
    for x in range(0, number_of_ints):
        int_subkey += str(random.randbelow(10))
        x += 1
    return int_subkey


def generate_random_letters(number_of_letters):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    char_subkey = ""
    for x in range(0, number_of_letters):
        random_substring = random.randbelow(len(letters))
        char_subkey += letters[random_substring:random_substring+1]
        x += 1
    return char_subkey


def generate_random_symbols(number_of_symbols):
    symbols = "!@#$%+=?&*()"
    symbol_subkey= ""
    for x in range(0, number_of_symbols):
        random_substring = random.randbelow(len(symbols))
        symbol_subkey += symbols[random_substring:random_substring+1]
        x += 1
    return symbol_subkey


def shuffle_sequence(key):
    key = list(key)
    random.SystemRandom().shuffle(key)
    return ''.join(key)


def generate_random_key(key_length, num_of_ints, num_of_letters, num_of_syms):
    key = ""
    if key_length > 0:
        if num_of_ints and num_of_ints > 0:
            key += generate_random_ints(num_of_ints)
        if num_of_letters and num_of_letters > 0:
            key += generate_random_letters(num_of_letters)
        if num_of_syms and num_of_syms > 0:
            key += generate_random_symbols(num_of_syms)
    key = shuffle_sequence(key)
    return key
