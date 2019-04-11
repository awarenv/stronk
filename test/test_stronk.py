import unittest
import stronk

from stronk import stronk
from unittest.mock import MagicMock


class stronkTest(unittest.TestCase):
    """ Test suite for the stronk module """

    def setUp(self):
        self.key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        self.mock = MagicMock()
        self.mock[0] = stronk._shuffle_key(self.key)

    def test_shuffle_key_returns_shuffled_key(self):
        self.assertNotEqual(self.mock[0], self.key)

    def test_default_key_generation_is_one_key(self):
        self.assertEqual(len(stronk.generate_random_keys()), 1)

    def test_default_key_generation_key_length_is_16(self):
        self.assertEqual(len(stronk.generate_random_keys()[0]), 16)

    def test_generate_max_100_keys(self):
        self.assertEqual(len(stronk.generate_random_keys(100)), 100)

    def test_error_returns_correct_message_if_keys_greater_than_100(self):
        self.assertEqual(stronk.generate_random_keys(
            101), "ERROR: Number of keys must be <= 100\n")

    def test_error_returns_correct_message_if_keys_is_zero(self):
        self.assertEqual(stronk.generate_random_keys(
            0), "ERROR: Number of keys must be non-zero and non-negative\n")

    def test_error_returns_correct_message_if_keys_is_negative(self):
        self.assertEqual(stronk.generate_random_keys(
            -100), "ERROR: Number of keys must be non-zero and non-negative\n")

    def test_error_returns_correct_message_if_key_length_greater_than_256(self):
        self.assertEqual(stronk.generate_random_keys(
            1, 257), "ERROR: Key length must be <= 256\n")

    def test_error_returns_correct_message_if_key_length_is_positive_and_less_than_16(self):
        self.assertEqual(stronk.generate_random_keys(
            1, 15), "ERROR: Key length must be non-zero and non-negative\n")

    def test_error_returns_correct_message_if_key_length_is_zero(self):
        self.assertEqual(stronk.generate_random_keys(
            1, 0), "ERROR: Key length must be non-zero and non-negative\n")

    def test_error_returns_correct_message_if_key_length_is_negative(self):
        self.assertEqual(stronk.generate_random_keys(
            1, -200), "ERROR: Key length must be non-zero and non-negative\n")

    def test_all_nonzero_and_nonnegative_errors_can_concatenate(self):
        self.assertEqual(stronk.generate_random_keys(
            0, 0), "ERROR: Number of keys must be non-zero and non-negative\nERROR: Key length must be non-zero and non-negative\n")

    def test_all_too_large_errors_can_concatenate(self):
        self.assertEqual(stronk.generate_random_keys(101, 257),
                         "ERROR: Number of keys must be <= 100\nERROR: Key length must be <= 256\n")
