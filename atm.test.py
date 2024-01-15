import unittest
from unittest.mock import patch, MagicMock
from main import ATM

class TestATM(unittest.TestCase):
    def setUp(self):
        self.atm = ATM()

    @patch('builtins.input', side_effect=['testuser', '1234'])
    @patch('main.auth.user_setup', return_value=True)
    def test_handle_new_account_success(self, mock_user_setup, mock_input):
        self.atm.handle_new_account()
        mock_user_setup.assert_called_once_with(username='testuser', password=1234)

    @patch('builtins.input', side_effect=['testuser', 'abcd'])
    def test_handle_new_account_invalid_password(self, mock_input):
        with self.assertRaises(ValueError):
            self.atm.handle_new_account()

    @patch('builtins.input', side_effect=['', '1234'])
    @patch('main.auth.user_setup', return_value=True)
    def test_handle_new_account_empty_username(self, mock_user_setup, mock_input):
        self.atm.handle_new_account()
        mock_user_setup.assert_called_once_with(username='', password=1234)

    @patch('builtins.input', side_effect=['testuser', ''])
    @patch('main.auth.user_setup', return_value=True)
    def test_handle_new_account_empty_password(self, mock_user_setup, mock_input):
        with self.assertRaises(ValueError):
            self.atm.handle_new_account()

if __name__ == '__main__':
    unittest.main()