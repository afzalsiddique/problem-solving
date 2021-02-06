# https://www.youtube.com/watch?v=snOaKR2xgZg
import unittest
from typing import List


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0: return 1
        if n==1: return x
        if n==2: return x*x
        if n<0: return 1/self.myPow(x,-n)
        res = self.myPow(x,n//2)
        res *= res
        if n%2==1:
            res*=x
        return res

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = 4.00000
        actual = sol.myPow(2,2)
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = 16.00000
        actual = sol.myPow(2,4)
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = 128
        actual = sol.myPow(2,7)
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = 9.26100
        actual = sol.myPow(2.1, 3)
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = 0.25000
        actual = sol.myPow(2,-2)
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        expected =54.83508
        actual = sol.myPow(0.44894, -5)
        self.assertEqual(expected, actual)
