from calculator.arithmetic import get_numbers
from unittest import TestCase
from unittest.mock import patch

class TestArithmetic(TestCase):
    @patch('builtins.input', return_value='6 12 3')
    def test_get_numbers(self, mock_input):
        result = get_numbers()
        expected = [6, 12, 3]
        self.assertEqual(result, expected)
