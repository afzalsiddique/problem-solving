# https://www.youtube.com/watch?v=ZYsuW19NMeo
import unittest
from bisect import *
from typing import List


class Solution:
    def jobScheduling(self, start: List[int], end: List[int], profit: List[int]) -> int:
        n = len(start)
        start, end, profit = zip(*sorted(zip(start, end, profit)))

        dp = [0 for _ in range(n + 1)]
        for i in reversed(range(n)):
            j = bisect_left(start, end[i])
            dp[i] = max(dp[i + 1], profit[i] + dp[j])

        return dp[0]

    def jobScheduling2(self, start: List[int], end: List[int], profit: List[int]) -> int:
        start, end, profit = zip(*sorted(zip(start, end, profit)))
        n=len(start)
        dp = [profit[i] for i in range(n)]
        for i in reversed(range(n)):
            j = bisect_left(start, end[i])
            if i==n-1:continue
            if j==n:
                dp[i]=max(dp[i],dp[i+1])
                continue
            dp[i]=max(dp[i+1], profit[i]+dp[j])
        return max(dp)

class MyTestCase(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        startTime = [1, 2, 3, 3]
        endTime = [3, 4, 5, 4]
        profit = [50, 10, 40, 70]
        actual = sol.jobScheduling(startTime, endTime,profit)
        expected = 120
        self.assertEqual(expected, actual)
    def test_2(self):
        sol = Solution()
        startTime = [1,2,3,4,6]
        endTime = [3,5,10,6,9]
        profit = [20,20,100,70,60]
        actual = sol.jobScheduling(startTime, endTime,profit)
        expected = 150
        self.assertEqual(expected, actual)
    def test_3(self):
        sol = Solution()
        startTime = [1,1,1]
        endTime = [2,3,4]
        profit = [5,6,4]
        actual = sol.jobScheduling(startTime, endTime,profit)
        expected = 6
        self.assertEqual(expected, actual)
