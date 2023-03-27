from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_right=[0]*(n+1) # "(n+1)" because [0,n] both are inclusive
        for i,x in enumerate(ranges):
            idx = max(0,i-x)
            max_right[idx]=x+i
        return self.jump(max_right)
    def jump(self,arr:List[int]): # leetcode 45
        n=len(arr)
        pos=n-1
        new_pos=n-1
        res=0
        while pos:
            for i in range(n):
                if arr[i]>=pos:
                    new_pos=i
                    res+=1
                    break
            if pos==new_pos: return -1
            pos=new_pos
        return res


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(1, get_sol().minTaps(5, [3,4,1,1,0,0]))
    def test02(self):
        self.assertEqual(-1, get_sol().minTaps(3, [0,0,0,0]))
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test8(self):
