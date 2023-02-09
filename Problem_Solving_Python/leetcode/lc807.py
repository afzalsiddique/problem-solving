from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        rowMax = [max(row) for row in grid]

        colMax = []
        for j in range(n):
            tmp=0
            for i in range(m):
                tmp=max(tmp,grid[i][j])
            colMax.append(tmp)

        res=0
        for i in range(m):
            for j in range(n):
                res+=min(rowMax[i],colMax[j])-grid[i][j]
        return res

class mycase(unittest.TestCase):
    def test01(self):
        self.assertEqual(35,get_sol().maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))
    def test02(self):
        self.assertEqual(0,get_sol().maxIncreaseKeepingSkyline([[0,0,0],[0,0,0],[0,0,0]]))
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
