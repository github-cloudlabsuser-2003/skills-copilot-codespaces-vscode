import unittest
from unittest.mock import patch
from io import StringIO
from app import calculator

class TestApp(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)

        @patch('builtins.input', side_effect=['1', '10', '5'])
        @patch('sys.stdout', new_callable=StringIO)
        def test_add(self, mock_stdout, mock_input):
            calculator()
            self.assertIn("10.0 + 5.0 = 15.0", mock_stdout.getvalue())
    
        @patch('builtins.input', side_effect=['2', '10', '5'])
        @patch('sys.stdout', new_callable=StringIO)
        def test_subtract(self, mock_stdout, mock_input):
            calculator()
            self.assertIn("10.0 - 5.0 = 5.0", mock_stdout.getvalue())
    
        @patch('builtins.input', side_effect=['3', '10', '5'])
        @patch('sys.stdout', new_callable=StringIO)
        def test_multiply(self, mock_stdout, mock_input):
            calculator()
            self.assertIn("10.0 * 5.0 = 50.0", mock_stdout.getvalue())
    
        @patch('builtins.input', side_effect=['4', '10', '5'])
        @patch('sys.stdout', new_callable=StringIO)
        def test_divide(self, mock_stdout, mock_input):
            calculator()
            self.assertIn("10.0 / 5.0 = 2.0", mock_stdout.getvalue())
    
        @patch('builtins.input', side_effect=['4', '10', '0'])
        @patch('sys.stdout', new_callable=StringIO)
        def test_divide_by_zero(self, mock_stdout, mock_input):
            calculator()
            self.assertIn("Error! Division by zero.", mock_stdout.getvalue())
    
        @patch('builtins.input', side_effect=['5', '10', '50'])
        @patch('sys.stdout', new_callable=StringIO)
        def test_percentage(self, mock_stdout, mock_input):
            calculator()
            self.assertIn("10.0 % of 50.0 = 5.0", mock_stdout.getvalue())
    
        @patch('builtins.input', side_effect=['6'])
        @patch('sys.stdout', new_callable=StringIO)
        def test_invalid_input(self, mock_stdout, mock_input):
            calculator()
            self.assertIn("Invalid input", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()