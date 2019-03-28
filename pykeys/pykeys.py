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


def generate_random_key(key_length, num_of_ints=0, num_of_letters=0, num_of_syms=0):
    key = ""
    msg_suffix = "This lowers the security integrity of the generated key."
    msg_success = "Key generated without any security issues."
    msg = ""
    if key_length > 0:
        if num_of_ints and num_of_ints > 0:
            key += generate_random_ints(num_of_ints)
        else:
            msg += "WARNING: There are no numbers in the key. " + msg_suffix + "\n"
        if num_of_letters and num_of_letters > 0:
            key += generate_random_letters(num_of_letters)
        else:
            msg += "WARNING: There are no letters in the key. " + msg_suffix + "\n"
        if num_of_syms and num_of_syms > 0:
            key += generate_random_symbols(num_of_syms)
        else:
            msg += "WARNING: There are no symbols in the key. " + msg_suffix + "\n"
        key = shuffle_sequence(key)
        if msg is not "":
            print(msg)
            return msg
        else:
            print(msg_success)
            print(key)
            return key
    else:
        return "ERROR: Provide how many characters you want in the key."

generate_random_key(10)
generate_random_key(10, 3)
generate_random_key(10, 3, 4)
generate_random_key(10, 3, 4, 3)

