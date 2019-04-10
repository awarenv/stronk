"""
Pykeys module
"""

import secrets as random


class Pykeys():
    """
    Pykeys class
    """
    def __init__(self):
        self.key = ''
        self.keys = []
        self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        self.symbols = '!@#$%+=?&*()'
        self.character_type = 1


    def generate_random_keys(self, number_of_keys=1, key_length=16):
        """ Returns the generated keys """
        number_of_keys_iterator = 0
        while number_of_keys_iterator < number_of_keys:
            key_length_iterator = 0
            while key_length_iterator < key_length:
                self.key += self._generate_random_char()
                key_length_iterator += 1
            self.keys[number_of_keys_iterator] = self._shuffle_key(self.key)
            number_of_keys_iterator += 1
        return self.keys


    def generate_sha5_hash(self):
        """ Generate sha5 hash """
        return self


    def _shuffle_key(self, key):
        """ Returns the shuffled key """
        key = list(self.key)
        random.SystemRandom().shuffle(key)
        return ''.join(key)


    def _generate_random_char(self):
        """ Generate a random integer, letter, or symbol """
        self.character_type = random.randbelow(3)
        if self.character_type == 0:
            return random.randbelow(10)
        if self.character_type == 1:
            return random.randbelow(len(self.letters))
        if self.character_type == 2:
            return random.randbelow(len(self.symbols))
        return -1
