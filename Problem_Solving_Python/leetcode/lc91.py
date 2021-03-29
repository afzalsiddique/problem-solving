from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        di = {}
        def decode(s:str):
            n = len(s)
            if n==0:return 1
            if n==1:
                return 1 if s!='0' else 0
            if s in di:return di[s]
            ans = 0
            first,second = s[0],s[1]
            # considering one char
            if first!='0':
                ans+=decode(s[1:])
            # considering two chars
            if first=='1':
                ans+=decode(s[2:])
            elif first=='2' and second>='0' and second<='6':
                ans += decode(s[2:])
            di[s]=ans
            return di[s]

        return decode(s)


class mytestcase(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, Solution().numDecodings('12'))
    def test2(self):
        self.assertEqual(3, Solution().numDecodings('226'))
    def test3(self):
        self.assertEqual(0, Solution().numDecodings('0'))
    def test4(self):
        self.assertEqual(0, Solution().numDecodings('06'))
    def test5(self):
        self.assertEqual(433494437, Solution().numDecodings('111111111111111111111111111111111111111111'))
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
