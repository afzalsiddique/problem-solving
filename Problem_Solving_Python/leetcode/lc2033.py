import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        li = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                li.append(grid[i][j])
        li.sort()
        n=len(li)
        mid1,mid2 = None,None
        if n&1:
            mid1 = li[n//2]
        else:
            mid1 = li[n//2-1]
            mid2 = li[n//2]
        ans1,ans2 = float('inf'),float('inf')
        cur = 0
        flag1=True
        for a in li:
            if abs(a-mid1)%x==0:
                cur+=abs(a-mid1)//x
            else:
                flag1=False
        if flag1:
            ans1=cur
        cur = 0
        flag2=True
        if mid2:
            for a in li:
                if abs(a-mid2)%x==0:
                    cur+=abs(a-mid2)//x
                else:
                    flag2=False
        if flag2 and mid2:
            ans2 = cur
        if ans1==float('inf') and ans2==float('inf'):
            return -1
        return min(ans1,ans2)

class MyTestCase(unittest.TestCase):
    def test1(self):
        grid,x = [[2,4],[6,8]],  2
        Output= 4
        self.assertEqual(Output, get_sol().minOperations(grid,x))
    def test2(self):
        grid,x = [[1,5],[2,3]],  1
        Output= 5
        self.assertEqual(Output, get_sol().minOperations(grid,x))
    def test3(self):
        grid,x = [[1,2],[3,4]],  2
        Output= -1
        self.assertEqual(Output, get_sol().minOperations(grid,x))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
