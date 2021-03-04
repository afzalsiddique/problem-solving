import unittest
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        A.sort(), B.sort(), C.sort(), D.sort()
        n = len(A)
        cnt=0
        D_set = set(x for x in D)
        for i in range(n):
            for j in range(n):
                for k in range(n):

        return cnt

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.fourSumCount(A = [ 1, 2],
                                    B = [-2,-1],
                                    C = [-1, 2],
                                    D = [ 0, 2])
        expected = 2
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.fourSumCount(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.fourSumCount(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.fourSumCount(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.fourSumCount(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.fourSumCount(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.fourSumCount(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.fourSumCount(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.fourSumCount(0)
        expected = 0
        self.assertEqual(expected, actual)