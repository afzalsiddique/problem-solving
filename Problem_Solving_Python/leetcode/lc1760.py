# https://www.youtube.com/watch?v=5ET1d6PfbNU
import unittest
from typing import List
class Solution:
    def minimumSize(self, A, k):
        left, right = 1, max(A)
        while left < right:
            mid = (left + right) // 2
            if sum((a - 1) // mid for a in A) > k:
                left = mid + 1
            else:
                right = mid
        return left

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.minimumSize(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.minimumSize(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.minimumSize(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.minimumSize(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.minimumSize(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.minimumSize(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.minimumSize(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.minimumSize(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.minimumSize(0)
        expected = 0
        self.assertEqual(expected, actual)