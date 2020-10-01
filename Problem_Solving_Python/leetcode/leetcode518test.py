import unittest
from leetcode.leetcode518 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        amount = 5
        coins = [1,2,5]
        actual = solution.change(amount, coins)
        expected = 4
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        amount = 3
        coins = [2]
        actual = solution.change(amount, coins)
        expected = 0
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        amount = 10
        coins = [10]
        actual = solution.change(amount, coins)
        expected = 1
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
