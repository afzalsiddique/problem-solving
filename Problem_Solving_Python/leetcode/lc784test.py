import unittest
from leetcode.lc784 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = sorted(solution.letterCasePermutation('ab'))
        expected = sorted(['ab','Ab','aB','AB'])
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        actual = sorted(solution.letterCasePermutation('a1b2'))
        expected = sorted(["a1b2","a1B2","A1b2","A1B2"])
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        actual = sorted(solution.letterCasePermutation("3z4"))
        expected = sorted(["3z4","3Z4"])
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        actual = sorted(solution.letterCasePermutation("12345"))
        expected = sorted(["12345"])
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        actual = sorted(solution.letterCasePermutation("0"))
        expected = sorted(["0"])
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        actual = sorted(solution.letterCasePermutation("00a"))
        expected = sorted(["00a","00A"])
        self.assertEqual(expected, actual)

    def test_7(self):
        solution = Solution()
        actual = sorted(solution.letterCasePermutation("a00"))
        expected = sorted(["a00","A00"])
        self.assertEqual(expected, actual)

