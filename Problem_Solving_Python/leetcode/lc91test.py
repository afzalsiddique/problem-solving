import unittest
from leetcode.lc91 import *
class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        s = '11'
        actual = solution.numDecodings(s)
        expected = 2
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        s = '10'
        actual = solution.numDecodings(s)
        expected = 1
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        s = '01'
        actual = solution.numDecodings(s)
        expected = 0
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        s = '0002'
        actual = solution.numDecodings(s)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        s = '27'
        actual = solution.numDecodings(s)
        expected = 1
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        s = '72'
        actual = solution.numDecodings(s)
        expected = 1
        self.assertEqual(expected, actual)


    def test_7(self):
        solution = Solution()
        s = '121'
        actual = solution.numDecodings(s)
        expected = 3
        self.assertEqual(expected, actual)

    def test_8(self):
        solution = Solution()
        s = '811'
        actual = solution.numDecodings(s)
        expected = 2
        self.assertEqual(expected, actual)

    def test_9(self):
        solution = Solution()
        s = '181'
        actual = solution.numDecodings(s)
        expected = 2
        self.assertEqual(expected, actual)

    def test_10(self):
        solution = Solution()
        s = '118'
        actual = solution.numDecodings(s)
        expected = 3
        self.assertEqual(expected, actual)

    def test_11(self):
        solution = Solution()
        s = '2262'
        actual = solution.numDecodings(s)
        expected = 3
        self.assertEqual(expected, actual)

    def test_12(self):
        solution = Solution()
        s = '226'
        actual = solution.numDecodings(s)
        expected = 3
        self.assertEqual(expected, actual)

    def test_13(self):
        solution = Solution()
        s = '0'
        actual = solution.numDecodings(s)
        expected = 0
        self.assertEqual(expected, actual)

    def test_14(self):
        solution = Solution()
        s = '230'
        actual = solution.numDecodings(s)
        expected = 0
        self.assertEqual(expected, actual)
    def test_15(self):
        solution = Solution()
        s = '227257'
        actual = solution.numDecodings(s)
        expected = 4
        self.assertEqual(expected, actual)