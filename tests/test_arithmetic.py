from calculator.arithmetic import get_numbers, addition, subtraction, multiplication, division
from unittest import TestCase
from unittest.mock import patch


class TestArithmetic(TestCase):
    @patch('builtins.input', return_value='6 12 3')
    def test_get_numbers(self, mock_input):
        result = get_numbers()
        expected = [6, 12, 3]
        self.assertEqual(result, expected)

    # Menguji inputan bukan spasi sebagai pemisah
    @patch('builtins.input', return_value='6,12,3')
    def test_get_numbers_with_comma_as_separator(self, mock_input):
        with self.assertRaises(ValueError) as context:
            get_numbers()
        self.assertEqual(str(context.exception), "Masukan angka dengan spasi sebagai pemisah dan gunakan '.' "
                                                 "ketika menggunakan decimal.")

    # dan "." bukan sebagai decimal.
    @patch('builtins.input', return_value='6,1 3')
    def test_get_numbers_not_use_dot_as_decimal(self, mock_input):
        with self.assertRaises(ValueError) as context:
            get_numbers()
        self.assertEqual(str(context.exception), "Masukan angka dengan spasi sebagai pemisah dan gunakan '.' "
                                                 "ketika menggunakan decimal.")

    def test_addition_positive_number(self):
        numbers = [6, 12]
        result = addition(numbers)
        expected = 18
        self.assertEqual(result, expected)

    def test_addition_negative_number(self):
        numbers = [-6, -12]
        result = addition(numbers)
        expected = -18
        self.assertEqual(result, expected)

    def test_addition_mix_number(self):
        numbers = [6, -12]
        result = addition(numbers)
        expected = -6
        self.assertEqual(result, expected)

    def test_subtraction_positive_number(self):
        numbers = [6, 12]
        result = subtraction(numbers)
        expected = -6
        self.assertEqual(result, expected)

    def test_subtraction_negative_number(self):
        numbers = [-6, -12]
        result = subtraction(numbers)
        expected = 6
        self.assertEqual(result, expected)

    def test_subtraction_mix_number(self):
        numbers = [6, -12]
        result = subtraction(numbers)
        expected = 18
        self.assertEqual(result, expected)

    def test_multiplication_positive_number(self):
        numbers = [10, 12]
        result = multiplication(numbers)
        expected = 120
        self.assertEqual(result, expected)

    def test_multiplication_negative_number(self):
        numbers = [-10, -12]
        result = multiplication(numbers)
        expected = 120
        self.assertEqual(result, expected)

    def test_multiplication_mix_number(self):
        numbers = [10, -12]
        result = multiplication(numbers)
        expected = -120
        self.assertEqual(result, expected)

    def test_division_positive_number(self):
        numbers = [12, 2]
        result = division(numbers)
        expected = 6
        self.assertEqual(result, expected)

    def test_division_negative_number(self):
        numbers = [-12, -2]
        result = division(numbers)
        expected = 6
        self.assertEqual(result, expected)

    def test_division_mix_number(self):
        numbers = [-12, 2]
        result = division(numbers)
        expected = -6
        self.assertEqual(result, expected)

    def test_division_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as context:
            numbers = [12, 0]
            division(numbers)
        self.assertEqual(str(context.exception), "Anda tidak bisa membagi bilangan dengan angka 0!")