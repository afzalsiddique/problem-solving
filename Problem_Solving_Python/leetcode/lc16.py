from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    def threeSumClosest(self, A: List[int], target: int) -> int:
        n=len(A)
        A.sort()
        res=float('inf')
        for i in range(n-2):
            l,r=i+1,n-1
            while l<r:
                s=A[i]+A[l]+A[r]
                if s==target:
                    return s
                if s>target:
                    r-=1
                else:
                    l+=1
                if abs(s-target)<abs(res-target):
                    res=s
        return res
class Solution2:
    def threeSumClosest(self, A: List[int], target: int) -> int:
        n = len(A)
        A.sort()
        res=float('inf')
        diff = float('inf')
        for i in range(n-2):
            l, r = i + 1, n - 1
            while l<r:
                s = A[i] + A[l] + A[r]
                if abs(s - target) < diff:
                    diff = abs(s - target)
                    res = s
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    return s
        return res


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(2, get_sol().threeSumClosest([-1,2,1,-4],1))
    def test02(self):
        self.assertEqual(3, get_sol().threeSumClosest([0,1,2], 3))
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
