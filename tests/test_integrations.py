from unittest import TestCase, mock
from unittest.mock import patch
from main import main


class TestIntegrations(TestCase):
    @patch('builtins.input', side_effect='q')
    def test_quit_program(self, mock_input_ops):
        with self.assertRaises(SystemExit):
            main()

    @patch('main.get_numbers', return_value=[2.0,2.1])  # value
    @patch('main.input', return_value='1')  # operations
    def test_addition(self, mock_input_ops, mock_value):
        with mock.patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with('Hasil: 4.1')
