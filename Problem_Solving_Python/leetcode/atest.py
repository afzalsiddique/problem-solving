import unittest
from leetcode.a import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        number = "1-23-45 6"
        actual = solution.reformatNumber(number)
        expected = "123-456"
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        number = "123 4-567"
        actual = solution.reformatNumber(number)
        expected = "123-45-67"
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        number = "123 4-5678"
        expected = "123-456-78"
        actual = solution.reformatNumber(number)
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        number = "   1  2---"
        expected = "12"
        actual = solution.reformatNumber(number)
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        number = "12"
        expected = "12"
        actual = solution.reformatNumber(number)
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        number = "--17-5 229 35-39475 "
        expected = "175-229-353-94-75"
        actual = solution.reformatNumber(number)
        self.assertEqual(expected, actual)