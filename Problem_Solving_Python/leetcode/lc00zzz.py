from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        def within(x:int,y:int)->bool:
            return 0<=x<len(mat) and 0<=y<len(mat[0])
        def get_4d_moves(x:int, y:int)->List[tuple[int,int]]:
            return [(x+dx,y+dy) for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)] if within(x+dx,y+dy)]

        @cache
        def dp(i,j):
            res=1
            for x,y in get_4d_moves(i,j):
                if mat[x][y]>mat[i][j]:
                    res=max(res,1+dp(x,y))
            return res

        res=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
               res=max(res,dp(i,j))
        return res




class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(4, get_sol().longestIncreasingPath( [[9,9,4],[6,6,8],[2,1,1]]))
    def test02(self):
        self.assertEqual(4, get_sol().longestIncreasingPath( [[3,4,5],[3,2,6],[2,2,1]]))
    def test03(self):
        self.assertEqual(1, get_sol().longestIncreasingPath( [[1]]))
    def test04(self):
        self.assertEqual(140, get_sol().longestIncreasingPath( [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]))
