from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # works because All the values of nums are unique
    def arrayNesting(self, A: List[int]) -> int:
        n=len(A)
        res=0
        vis=[False]*n
        for i in range(n):
            # if vis[i]: continue
            cnt=0
            while not vis[i]:
                vis[i]=True
                cnt+=1
                i=A[i]
            res=max(res,cnt)
        return res

class Solution2:
    # works because All the values of nums are unique
    def arrayNesting(self, A: List[int]) -> int:
        A=[x+1 for x in A] # make range [1,n]
        n=len(A)
        res=0
        for i in range(n):
            # if A[i]<0: continue
            cnt=0
            while A[i]>0:
                A[i]*=(-1)
                cnt+=1
                i=abs(A[i])-1
            res=max(res,cnt)
        return res


class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(4,get_sol().arrayNesting( [5,4,0,3,1,6,2]))
    def test02(self):
        self.assertEqual(1,get_sol().arrayNesting([0,1,2]))
    # def test03(self):
