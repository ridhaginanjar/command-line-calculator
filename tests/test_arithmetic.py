from calculator.arithmetic import get_numbers
from unittest import TestCase
from unittest.mock import patch

class TestArithmetic(TestCase):
    @patch('builtins.input', return_value='6 12 3')
    def test_get_numbers(self, mock_input):
        result = get_numbers()
        expected = [6, 12, 3]
        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=ValueError("Invalid Input!"))
    def test_get_numbers_with_comma(self, mock_input):
        with self.assertRaises(ValueError) as context:
            get_numbers()
        self.assertEqual(str(context.exception), "Invalid Input!")




