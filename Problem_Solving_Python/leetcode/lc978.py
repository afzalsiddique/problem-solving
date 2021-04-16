import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n=len(arr)
        plus,minus=1,1
        maxx=1
        for i in range(1,n):
            if arr[i]<arr[i-1]:
                plus=minus+1
                minus=1
            elif arr[i]>arr[i-1]:
                minus=plus+1
                plus=1
            else:
                minus=1
                plus=1
            maxx=max(maxx,plus,minus)
        return maxx

    def maxTurbulenceSize2(self, arr: List[int]) -> int:
        n=len(arr)
        dp=[[1]*2 for i in range(n)]
        for i in range(1,n):
            if arr[i]<arr[i-1]:
                dp[i][0]=max(dp[i][0],1+dp[i-1][1])
            elif arr[i]>arr[i-1]:
                dp[i][1]=max(dp[i][1],1+dp[i-1][0])
        # print(dp)
        return max(map(max,dp))
class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(5,Solution().maxTurbulenceSize( [9,4,2,10,7,8,8,1,9]))
    def test2(self):
        self.assertEqual(2,Solution().maxTurbulenceSize( [4,8,12,16]))
    def test3(self):
        self.assertEqual(1,Solution().maxTurbulenceSize( [100]))
    def test4(self):
        self.assertEqual(1,Solution().maxTurbulenceSize( [9,9]))