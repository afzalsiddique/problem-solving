import unittest
from leetcode.lc1143 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        text1 = 'abcdefg'
        text2 = 'chfg'
        actual = solution.longestCommonSubsequence(text1, text2)
        expected = 3
        self.assertEqual(expected, actual)


    def test_2(self):
        solution = Solution()
        text1 = 'abcde'
        text2 = 'ace'
        actual = solution.longestCommonSubsequence(text1, text2)
        expected = 3
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        text1 = "oxcpqrsvwf"
        text2 = "shmtulqrypy"
        actual = solution.longestCommonSubsequence(text1, text2)
        expected = 2
        self.assertEqual(expected, actual)