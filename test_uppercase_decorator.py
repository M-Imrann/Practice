import unittest
from unittest.mock import Mock
from uppercase_decorator import greeting, uppercase_decorator


class TestUppercaseDecorator(unittest.TestCase):
    '''
    The class is for testing the Uppercase Decorator.
    '''
    def test_greeting_function(self):
        '''
        test case to test the greeting function.
        '''
        result = greeting()
        self.assertEqual(result, "HEY, I AM MUHAMMAD IMRAN.")

    def test_decorator(self):
        '''
        test case to test the decorator function.
        '''
        mock_func = Mock()
        mock_func.return_value = "This is the mock Function"

        decorated = uppercase_decorator(mock_func)

        result = decorated()
        mock_func.assert_called_once()

        self.assertEqual(result, "THIS IS THE MOCK FUNCTION")


if __name__ == "__main__":
    unittest.main()
