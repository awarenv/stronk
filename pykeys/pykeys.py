"""
Pykeys module
"""

import secrets as random


class Pykeys():
    """
    Pykeys class
    """
    def __init__(self):
        self.char_subkey = ''
        self.int_subkey = ''
        self.symbol_subkey = ''
        self.key = ''


    def generate_random_keys(self, number_of_keys=1, key_length=16, num_of_ints=0,
                             num_of_letters=0, num_of_syms=0):
        """ Returns the response for generating the keys """
        response = {}
        key = ''
        msg_suffix = 'This lowers the security integrity of the generated key.'
        msg = ''
        response['messages'] = {}
        response['messages']['statuses'] = {}
        response['messages']['statuses']['keys'] = 'No keys were generated.'
        response['messages']['error'] = ''
        response['keys'] = [None] * number_of_keys
        k = 0
        while k < number_of_keys:
            if key_length > 0:
                key = ''
                if num_of_ints and num_of_ints > 0:
                    key += self._generate_random_chars(key_length, 0)
                else:
                    response['messages']['statuses']['numbers'] = 'WARNING: There are no ' + \
                        'numbers in the key. ' + msg_suffix
                if num_of_letters and num_of_letters > 0:
                    key += self._generate_random_chars(key_length, 1)
                else:
                    response['messages']['statuses']['letters'] = 'WARNING: There are no ' + \
                        'letters in the key. ' + msg_suffix
                if num_of_syms and num_of_syms > 0:
                    key += self._generate_random_chars(key_length, 2)
                else:
                    response['messages']['statuses']['symbols'] = 'WARNING: There are no ' + \
                        'symbols in the key. ' + msg_suffix
                if (num_of_ints and num_of_letters and num_of_letters) == 0:
                    key += self._generate_random_chars(key_length, 1)
                else:
                    key = ''
                key = self._shuffle_key(key)
                response['keys'][k] = key
                response['messages']['statuses']['keys'] = msg
            else:
                response['messages']['error'] = 'ERROR: Provide how many characters you ' + \
                    'want in the key.'
            k += 1
        return response


    def generate_sha5_hash(self):
        """ Generate sha5 hash """
        return self


    def _shuffle_key(self, key):
        """ Returns the shuffled key """
        key = list(self.key)
        random.SystemRandom().shuffle(key)
        return ''.join(key)


    def _generate_random_chars(self, number_of_chars, character_type):
        """ Returns a string of random characters or an error message """
        error_message = 'ERROR: Number of characters to generate is less than 1.'
        result = ''
        if number_of_chars > 0:
            character_dict = {
                0: self._generate_random_ints,
                1: self._generate_random_letters,
                2: self._generate_random_symbols
            }
            if character_type:
                result = character_dict[character_type](number_of_chars)
            else:
                result = character_dict[1](number_of_chars)
        else:
            return error_message
        return result


    def _generate_random_ints(self, number_of_ints):
        """ Returns a string of random ints """
        self.int_subkey = ''
        for iterator in range(0, number_of_ints):
            int_subkey += str(random.randbelow(10))
            iterator += 1
        return self.int_subkey


    def _generate_random_letters(self, number_of_letters):
        """ Returns a string of random letters, uppercase and lowercase """
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        self.char_subkey = ''
        for iterator in range(0, number_of_letters):
            random_substring = random.randbelow(len(letters))
            char_subkey += letters[random_substring:random_substring+1]
            iterator += 1
        return self.char_subkey


    def _generate_random_symbols(self, number_of_symbols):
        """ Returns a string of random symbols """
        symbols = '!@#$%+=?&*()'
        self.symbol_subkey = ''
        for iterator in range(0, number_of_symbols):
            random_substring = random.randbelow(len(symbols))
            symbol_subkey += symbols[random_substring:random_substring+1]
            iterator += 1
        return self.symbol_subkey
