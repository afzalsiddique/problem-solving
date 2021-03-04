######### TLE #######
##### need to include binary search ##########
import unittest
from typing import List


class Job:
    def __init__(self, start, end, profit):
        self.dur = (start, end)
        self.profit = profit

    def __repr__(self):
        return str(self.dur[0]) + " " + str(self.dur[1]) + " " + str(self.profit)


class Solution:

    def helper(self, jobs: List[Job]):
        def overlap(a, b):  # a and b are tuples -> (start,end)
            if a[1] > b[1]:
                a, b = b, a
            if b[0] >= a[1]:
                return False
            return True

        n = len(jobs)
        jobs.sort(key=lambda x: x.dur[1])  # sort by endTime
        dp = [job.profit for job in jobs]
        for i in range(1, n):
            for j in range(0, i):
                dur_i = jobs[i].dur
                dur_j = jobs[j].dur
                pro_i = jobs[i].profit
                if not overlap(dur_i, dur_j):
                    dp[i] = max(dp[i], dp[j] + pro_i)
        return max(dp)

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for i in range(len(startTime)):
            jobs.append(Job(startTime[i], endTime[i], profit[i]))
        return self.helper(jobs)


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.jobScheduling(startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70])
        expected = 120
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.jobScheduling(startTime=[1, 2, 3, 4, 6], endTime=[3, 5, 10, 6, 9], profit=[20, 20, 100, 70, 60])
        expected = 150
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4])
        expected = 6
        self.assertEqual(expected, actual)
