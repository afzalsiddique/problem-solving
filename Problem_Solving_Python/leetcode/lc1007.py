import itertools;from itertools import accumulate; from math import floor,ceil,sqrt,log2; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        minn=float('inf')
        for val in range(1,6+1):
            cnt,flag=0,True
            for i in range(n):
                if A[i]==val: continue
                if B[i]==val:
                    cnt+=1
                else:
                    flag=False
                    break
            if flag:minn=min(minn,cnt)
        for val in range(1,6+1):
            cnt,flag=0,True
            for i in range(n):
                if B[i]==val: continue
                if A[i]==val:
                    cnt+=1
                else:
                    flag=False
                    break
            if flag:minn=min(minn,cnt)
        return -1 if minn==float('inf') else minn

class Tester(unittest.TestCase):
    def test1(self):
        A = [2,1,2,4,2,2]
        B = [5,2,6,2,3,2]
        Output= 2
        self.assertEqual(Output,get_sol().minDominoRotations(A, B))
    def test2(self):
        A = [3,5,1,2,3]
        B = [3,6,3,3,4]
        Output= -1
        self.assertEqual(Output,get_sol().minDominoRotations(A, B))
    def test3(self):
        A = [1,2,1,1,1,2,2,2]
        B = [2,1,2,2,2,2,2,2]
        Output= 1
        self.assertEqual(Output,get_sol().minDominoRotations(A, B))
