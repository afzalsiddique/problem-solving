from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        def overlapping(l1,r1,l2,r2):
            return min(r1,r2)>max(l1,l2)
        n=len(positions)
        res=[]
        maxx=float('-inf')
        li = []
        for i in range(n):
            curmax=0
            l1,h1=positions[i]
            r1=l1+h1
            for l2,r2,h2 in li:
                if overlapping(l1,r1,l2,r2):
                    curmax=max(curmax,h2)

            newHeight=curmax+h1
            li.append([l1,r1,newHeight])
            maxx=max(maxx,newHeight)
            res.append(maxx)
        return res


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([2,5], get_sol().fallingSquares([[1,2],[2,3]]))
    def test2(self):
        self.assertEqual([2,5,5], get_sol().fallingSquares([[1,2],[2,3],[6,1]]))
    def test3(self):
        self.assertEqual([100,100], get_sol().fallingSquares([[100,100],[200,100]]))
    def test4(self):
        self.assertEqual([1,10,18], get_sol().fallingSquares([[2,1],[2,9],[1,8]]))
    # def test5(self):
    # def test6(self):
    # def test7(self):

