import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/count-servers-that-communicate/discuss/436130/C%2B%2B-Simple-Preprocessing
    def countServers(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        rows=[0 for _ in range(m)]
        cols=[0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rows[i]+=1
                    cols[j]+=1
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (rows[i]>1 or cols[j]>1):
                    x='debug'
                    ans+=1
        return ans


class tester(unittest.TestCase):
    def test_1(self):
        grid = [[1,0],[0,1]]
        Output= 0
        self.assertEqual(Output,get_sol().countServers(grid))
    def test_2(self):
        grid = [[1,0],[1,1]]
        Output= 3
        self.assertEqual(Output,get_sol().countServers(grid))
    def test_3(self):
        grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
        Output= 4
        self.assertEqual(Output,get_sol().countServers(grid))
    def test_4(self):
        grid = [[1,0,0,1,0],[0,0,0,0,0],[0,0,0,1,0]]
        Output= 3
        self.assertEqual(Output,get_sol().countServers(grid))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
