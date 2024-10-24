from unittest import TestCase
from unittest.mock import patch
from main import main

class TestIntegrations(TestCase):
    @patch('builtins.input', return_value='q')
    def test_quit_program(self, mock_input):
        with self.assertRaises(SystemExit):
            main()
