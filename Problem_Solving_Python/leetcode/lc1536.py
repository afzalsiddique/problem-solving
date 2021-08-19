from itertools import accumulate; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/discuss/768076/Min-Adjacent-Swaps-to-Sort-the-array-of-INTEGERS-with-Proof/640125
    def minSwaps(self, grid: List[List[int]]) -> int:
        n=len(grid)
        zeros=[]
        for row in grid:
            cnt=0
            for col in reversed(row):
                if col==0: cnt+=1
                else: break
            zeros.append(cnt)
        ans=0
        for i in range(n):
            target=n-i-1
            j=i
            while j<n and zeros[j]<target:
                j+=1
            if j==n: return -1
            while j>i:
                zeros[j],zeros[j-1]=zeros[j-1],zeros[i]
                j-=1
                ans+=1
        return ans

class MyTestCase(unittest.TestCase):
    def test_1(self):
        grid = [[0,0,1],[1,1,0],[1,0,0]]
        Output= 3
        self.assertEqual(Output, get_sol().minSwaps(grid))
    def test_2(self):
        grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
        Output= -1
        self.assertEqual(Output, get_sol().minSwaps(grid))
    def test_3(self):
        grid = [[1,0,0],[1,1,0],[1,1,1]]
        Output= 0
        self.assertEqual(Output, get_sol().minSwaps(grid))
    def test_4(self):
        grid = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
        Output= 2
        self.assertEqual(Output, get_sol().minSwaps(grid))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):