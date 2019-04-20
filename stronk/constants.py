"""
Constants
"""

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
SYMBOLS = '!@#$%+=?&*()'
MAX_KEY_NUMBER = 100
MAX_KEY_LENGTH = 256
MIN_KEY_NUMBER = 1
MIN_KEY_LENGTH = 16
__ERROR__ = {
    'MAX_KEY_NUMBER': 'ERROR: Number of keys must be <= 100\n',
    'POSITIVE_KEY_NUMBER': 'ERROR: Number of keys must be non-zero and non-negative\n',
    'MAX_KEY_LENGTH': 'ERROR: Key length must be <= 256\n',
    'POSITIVE_KEY_LENGTH': 'ERROR: Key length must be non-zero and non-negative\n'
}
INTEGERS = 10
PROBABILITY_FACTOR = 13

def max_key_number_error():
    """
    max_key_number_error()

    @return (String): The error message.
    """
    return __ERROR__['MAX_KEY_NUMBER']


def min_key_number_error():
    """
    min_key_number_error()

    @return (String): The error message.
    """
    return __ERROR__['POSITIVE_KEY_NUMBER']


def max_key_length_error():
    """
    max_key_length_error()

    @return (String): The error message.
    """
    return __ERROR__['MAX_KEY_LENGTH']


def min_key_length_error():
    """
    min_key_length_error()

    @return (String): The error message.
    """
    return __ERROR__['POSITIVE_KEY_LENGTH']
