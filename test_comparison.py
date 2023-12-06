import unittest
from random import choice
from string import ascii_lowercase
from task_comparison import comparison

class ComparisonTests(unittest.TestCase):

    def test_regression(self):
        self.assertTrue(comparison('abcdfgh', 'abc'))

    def test_full_check(self):
        self.assertFalse(comparison('ygeabcfd', 'abcd'))

    def test_random(self):
        for i in range(1000):
            x = ''.join(choice(ascii_lowercase) for _ in range(1000))
            y = ''.join(choice(ascii_lowercase) for _ in range(3))
            z = comparison(x, y)
            self.assertEqual(z, y in x)
            
    def test_uppercase(self):
        self.assertFalse(comparison('aBcdfgh', 'abc'))

if __name__ == '__main__':
    unittest.main()
