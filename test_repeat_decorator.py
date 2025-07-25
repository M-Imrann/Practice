import unittest
from repeat_decorator import greeting


class TestRepeatDecorator(unittest.TestCase):
    '''
    The class is for testing the Repeat Decorator.
    '''

    def test_greeting_function(self):
        '''
        test case to test the greeting function.
        '''
        result = greeting("Ali")
        expected = ['Hey Ali', 'Hey Ali', 'Hey Ali']
        self.assertEqual(result, expected)

    def test_greeting_repeat_count(self):
        result = greeting("Test")
        self.assertEqual(len(result), 3)
        self.assertTrue(all(r == "Hey Test" for r in result))


if __name__ == "__main__":
    unittest.main()
