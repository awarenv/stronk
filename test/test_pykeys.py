import unittest
import pykeys.pykeys as pykeys

class TestPykeys(unittest.TestCase):

    def test_generate_random_ints_success(self):
        number_of_ints = 10
        result = pykeys.generate_random_ints(number_of_ints)
        self.assertIsNot(result, None)
        self.assertEqual(len(result), 10)

    def test_generate_random_ints_returns_false_if_zero_is_passed(self):
        number_of_ints = 0
        result = pykeys.generate_random_ints(number_of_ints)
        self.assertEqual(result, False)

    def test_generate_random_ints_returns_error_msg_if_string_is_passed(self):
        invalid_argument = 'abc'
        error = 'ERROR'
        result = pykeys.generate_random_ints(invalid_argument)
        self.assertEqual(result, error)

    def test_generate_random_letters_success(self):
        number_of_letters = 10
        result = pykeys.generate_random_letters(number_of_letters)
        self.assertIsNot(result, None)
        self.assertEqual(len(result), 10)

    def test_generate_random_letters_returns_false_if_zero_is_passed(self):
        number_of_letters = 0
        result = pykeys.generate_random_letters(number_of_letters)
        self.assertEqual(result, False)

    def test_generate_random_letters_returns_error_msg_if_string_is_passed(self):
        invalid_argument = 'abc'
        error = 'ERROR'
        result = pykeys.generate_random_letters(invalid_argument)
        self.assertEqual(result, error)

    def test_generate_random_symbols_success(self):
        number_of_symbols = 10
        result = pykeys.generate_random_symbols(number_of_symbols)
        self.assertIsNot(result, None)
        self.assertEqual(len(result), 10)

    def test_generate_random_symbols_returns_false_if_zero_is_passed(self):
        number_of_symbols = 0
        result = pykeys.generate_random_symbols(number_of_symbols)
        self.assertEqual(result, False)

    def test_generate_random_symbols_returns_error_msg_if_string_is_passed(self):
        invalid_argument = 'abc'
        error = 'ERROR'
        result = pykeys.generate_random_symbols(invalid_argument)
        self.assertEqual(result, error)

    def test_shuffle_key_success(self):
        return True

    def test_shuffle_key_fail(self):
        return True

    def test_generate_random_keys_success(self):
        return True

    def test_generate_random_keys_fail(self):
        return True

if __name__ == '__main__':
    unittest.main()
