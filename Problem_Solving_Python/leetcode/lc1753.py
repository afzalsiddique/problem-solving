# contest 227
import unittest
from typing import List


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        li = [a,b,c]
        li.sort()
        c = li[0] # 3rd highest
        b = li[1] # 2nd highest
        a = li[2] # highest
        if a<=b+c:
            return (a+b+c)//2
        a = b+c
        return (a+b+c)//2

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.maximumScore(a = 2, b = 4, c = 6)
        expected = 6
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.maximumScore(a = 4, b = 4, c = 6)
        expected = 7
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.maximumScore(a = 4, b = 5, c = 6)
        expected = 7
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.maximumScore(15,4,6)
        expected = 10
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.maximumScore(a = 1, b = 8, c = 8)
        expected = 8
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.maximumScore(6,2,1)
        expected = 3
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.maximumScore(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.maximumScore(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.maximumScore(0)
        expected = 0
        self.assertEqual(expected, actual)