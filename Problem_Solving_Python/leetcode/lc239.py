# https://www.youtube.com/watch?v=LiSdD3ljCIE
from heapq import *
import unittest
from collections import *
from typing import List



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq, n= [], len(nums)
        res = []
        for i in range(k-1):
            heappush(pq, (-nums[i],i)) # pq is (-val,idx)
        for i in range(n-k+1):
            heappush(pq, (-nums[i+k-1], i+k-1))
            val, idx = pq[0]
            res.append(val*(-1)) # append the max val
            while pq and pq[0][1] <= i: # remove the nodes which are dated
                heappop(pq)
        return res


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
        expected = [3,3,5,5,6,7]
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.maxSlidingWindow(nums = [1], k = 1)
        expected = [1]
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.maxSlidingWindow(nums = [1,-1], k = 1)
        expected = [1,-1]
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.maxSlidingWindow(nums = [9,11], k = 2)
        expected = [11]
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.maxSlidingWindow(nums = [4,-2], k = 2)
        expected = [4]
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.maxSlidingWindow([9,10,9,-7,-4,-8,2,-6],5)
        expected = [10,10,9,2]
        self.assertEqual(expected, actual)
