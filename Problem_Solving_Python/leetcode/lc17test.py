import unittest
from leetcode.lc17 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = solution.letterCombinations("23")
        expected = sorted(["ad","ae","af","bd","be","bf","cd","ce","cf"])
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        actual = solution.letterCombinations("2")
        expected = sorted(["a","b","c"])
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        actual = solution.letterCombinations("")
        expected = sorted([])
        self.assertEqual(expected, actual)