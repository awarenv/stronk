import unittest
from pykeys import pykeys

class PykeysTest(unittest.TestCase):
    """ Test suite for the Pykeys module """
    def setUp(self):
        self.key = pykeys.generate_random_keys(1, key_length=16)

    def test_shuffle_key_returns_shuffled_key(self):
        self.assertNotEquals(pykeys._shuffle_key(self.key), self.key)
