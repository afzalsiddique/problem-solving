from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum&1:
            return []
        res=[]
        x=2
        while finalSum>2*x:
            res.append(x)
            finalSum-=x
            x+=2
        res.append(finalSum)
        return res
class Solution2:
    # tle
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        @cache
        def recur(num):
            if num==0:
                return []
            res=[]
            for x in range(2,num+1,2):
                ans=recur(num-x)
                if x not in ans:
                    res=max(res,[x]+ans,key=lambda x:len(x))
            return res

        if finalSum&1:
            return []
        return recur(finalSum)
class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual([2,4,6], sorted(get_sol().maximumEvenSplit(12)))
    def test2(self):
        self.assertEqual([], sorted(get_sol().maximumEvenSplit(7)))
    def test3(self):
        self.assertEqual([2,6,8,12], sorted(get_sol().maximumEvenSplit(28)))
    def test4(self):
        self.assertEqual([2,6,8,12], sorted(get_sol().maximumEvenSplit(71252)))
    # def test5(self):
    # def test6(self):
