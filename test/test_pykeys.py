import unittest
import pykeys.pykeys as pykeys

class TestPykeys(unittest.TestCase):

    def test_generate_random_ints_success(self):
        number_of_ints = 10
        result = pykeys.generate_random_chars(number_of_ints)
        self.assertIsNot(result, None)
        self.assertEqual(len(result), 10)

    def test_generate_random_ints_returns_false_if_zero_is_passed(self):
        number_of_ints = 0
        result = pykeys.generate_random_chars(number_of_ints)
        self.assertEqual(result, False)

    def test_generate_random_ints_returns_error_msg_if_string_is_passed(self):
        invalid_argument = 'abc'
        error = 'ERROR'
        result = pykeys.generate_random_ints(invalid_argument)
        self.assertEqual(result, error)

    def test_generate_random_letters_success(self):
        number_of_letters = 10
        result = pykeys.generate_random_chars(number_of_letters)
        self.assertIsNot(result, None)
        self.assertEqual(len(result), 10)

    def test_generate_random_letters_returns_false_if_zero_is_passed(self):
        number_of_letters = 0
        result = pykeys.generate_random_chars(number_of_letters)
        self.assertEqual(result, False)

    def test_generate_random_letters_returns_error_msg_if_string_is_passed(self):
        invalid_argument = 'abc'
        error = 'ERROR'
        result = pykeys.generate_random_chars(invalid_argument)
        self.assertEqual(result, error)

    def test_generate_random_symbols_success(self):
        number_of_symbols = 10
        result = pykeys.generate_random_chars(number_of_symbols)
        self.assertIsNot(result, None)
        self.assertEqual(len(result), 10)

    def test_generate_random_symbols_returns_false_if_zero_is_passed(self):
        number_of_symbols = 0
        result = pykeys.generate_random_chars(number_of_symbols)
        self.assertEqual(result, False)

    def test_generate_random_symbols_returns_error_msg_if_string_is_passed(self):
        invalid_argument = 'abc'
        error = 'ERROR'
        result = pykeys.generate_random_chars(invalid_argument)
        self.assertEqual(result, error)

    def test_shuffle_key_success(self):
        key = "abcdefg"
        result = pykeys.shuffle_key(key)
        self.assertNotEqual(result, key)

    def test_shuffle_key_fail(self):
        key = "abcdefg"
        error = 'ERROR'
        result = pykeys.shuffle_key(key)
        self.assertEqual(result, error)

    def test_generate_random_keys_success(self):
        number_of_keys = 3
        key_length = 10
        result = pykeys.generate_random_keys(3, 10)
        self.assertEqual(result['number_of_keys'], 3)
        self.assertEqual(len(result['keys'])[0], 10)

    def test_generate_random_keys_fail(self):
        number_of_keys = 3
        key_length = 10
        error = 'ERROR'
        result = pykeys.generate_random_keys(3, 10)
        self.assertEqual(result['message'], error)
        self.assertNotEqual(result['number_of_keys'], 0)
        self.assertEqual(len(result['keys'])[0]. None)

if __name__ == '__main__':
    unittest.main()
