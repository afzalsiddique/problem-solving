from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def minimumRemoval(self, A: List[int]) -> int:
        n=len(A)
        A.sort()
        res=float('inf')
        pre=[0]+list(accumulate(A))
        for i in range(n-1):
            j=i+1
            total=0
            total+=pre[i+1]
            tmp1=(pre[-1]-pre[j])
            tmp2=A[j]*(n-j)
            total+=tmp1-tmp2
            res=min(res,total)
        total=pre[-1]-A[0]*n
        res=min(res,total)
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, get_sol().minimumRemoval([4,1,6,5]))
    def test2(self):
        self.assertEqual(7, get_sol().minimumRemoval([2,10,3,2]))
    def test3(self):
        self.assertEqual(3, get_sol().minimumRemoval([4,5,6]))
    # def test4(self):
    # def test5(self):
    # def test6(self):
