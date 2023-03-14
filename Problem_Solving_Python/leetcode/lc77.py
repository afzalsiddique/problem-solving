from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(i,k,path):
            if k==0:
                res.append(path)
                return
            if i>n: return
            backtrack(i+1,k-1,path+[i])
            backtrack(i+1,k,path[:])

        res=[]
        backtrack(1,k,[])
        return res

class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start,left,path):
            if left==0:
                res.append(path)
                return
            for i in range(start,n+1):
                backtrack(i+1,left-1,path+[i])

        res=[]
        backtrack(1,k,[])

        return res


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(sorted([ [2,4], [3,4], [2,3], [1,2], [1,3], [1,4], ]),sorted(get_sol().combine(4,2)))
    def test02(self):
        self.assertEqual(sorted([ [1,2], [1,3], [2,3] ]),sorted(get_sol().combine(3,2)))
    def test03(self):
        self.assertEqual(sorted([ [1], [2]]),sorted(get_sol().combine(2,1)))
