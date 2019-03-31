import secrets as random


response = {}

def generate_random_key(key_length, num_of_ints=0, num_of_letters=0, num_of_syms=0):
    key = ""
    msg_suffix = "This lowers the security integrity of the generated key."
    msg_success = "Key generated without any security issues."
    msg = ""
    response['message'] = "No keys were generated."
    response['keys'] = []
    if key_length > 0:
        key = ''
        key_dict = {
            'ints': _generate_random_chars,
            'letters': _generate_random_chars,
            'symbols': _generate_random_chars
        }
        if num_of_ints and num_of_ints > 0:
            key += key_dict['ints'](num_of_ints, 0)
        else:
            msg += "WARNING: There are no numbers in the key. " + msg_suffix + "\n"
        if num_of_letters and num_of_letters > 0:
            key += key_dict['letters'](num_of_letters, 1)
        else:
            msg += "WARNING: There are no letters in the key. " + msg_suffix + "\n"
        if num_of_syms and num_of_syms > 0:
            key += key_dict['symbols'](num_of_syms, 2)
        else:
            msg += "WARNING: There are no symbols in the key. " + msg_suffix + "\n"
        if (num_of_ints and num_of_letters and num_of_letters) == 0:
            key = _generate_random_chars(key_length, 1)
        else:
            key = ''
        key = shuffle_key(key)
        if msg is not "":
            print(msg)
            return msg
        else:
            print(msg_success)
            print(key)
            return key
    else:
        return "ERROR: Provide how many characters you want in the key."


def shuffle_key(key):
    key = list(key)
    random.SystemRandom().shuffle(key)
    return ''.join(key)


def _generate_random_chars(number_of_chars, character_type):
    error_message = 'ERROR: Number of characters to generate is less than 1.'
    result = ''
    if number_of_chars > 0:
        character_dict = {
            0: _generate_random_ints,
            1: _generate_random_letters,
            2: _generate_random_symbols
        }
        if character_type:
            result = character_dict[character_type](number_of_chars)
        else:
            result = character_dict[1](number_of_chars)
    else:
        return error_message
    return result


def _generate_random_ints(number_of_ints):
    int_subkey = ""
    for x in range(0, number_of_ints):
        int_subkey += str(random.randbelow(10))
        x += 1
    return int_subkey


def _generate_random_letters(number_of_letters):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    char_subkey = ""
    for x in range(0, number_of_letters):
        random_substring = random.randbelow(len(letters))
        char_subkey += letters[random_substring:random_substring+1]
        x += 1
    return char_subkey


def _generate_random_symbols(number_of_symbols):
    symbols = "!@#$%+=?&*()"
    symbol_subkey= ""
    for x in range(0, number_of_symbols):
        random_substring = random.randbelow(len(symbols))
        symbol_subkey += symbols[random_substring:random_substring+1]
        x += 1
    return symbol_subkey


generate_random_key(10)
generate_random_key(10, 3)
generate_random_key(10, 3, 4)
generate_random_key(10, 3, 4, 3)

