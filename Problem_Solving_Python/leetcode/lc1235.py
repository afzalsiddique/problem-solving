# https://www.youtube.com/watch?v=ZYsuW19NMeo
import unittest
from bisect import *
from typing import List


class Solution:
    def jobScheduling(self, start: List[int], end: List[int], profit: List[int]) -> int:
        n = len(start)
        start, end, profit = zip(*sorted(zip(start, end, profit)))
        jump = {i: bisect_left(start, end[i]) for i in range(n)}

        dp = [0 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i + 1], profit[i] + dp[jump[i]])

        return dp[0]


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        startTime = [1, 2, 3, 3]
        endTime = [3, 4, 5, 4]
        profit = [50, 10, 40, 70]
        actual = sol.jobScheduling(startTime, endTime,profit)
        expected = 120
        self.assertEqual(expected, actual)
