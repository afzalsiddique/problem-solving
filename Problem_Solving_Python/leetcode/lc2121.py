from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n=len(arr)
        di=defaultdict(list)
        preSumDi={}
        for idx,a in enumerate(arr):
            di[a].append(idx)
        for x in arr:
            if x not in preSumDi:
                li=di[x]
                preSumDi[x]=[0]+list(accumulate(li))

        res=[0]*n
        for i,x in enumerate(arr):
            li=di[x]
            pre=preSumDi[x]

            leftIdx=bisect_left(li,i)
            noOfItemsOnTheLeft=leftIdx
            leftSum=pre[leftIdx]
            tmp=i*noOfItemsOnTheLeft-leftSum
            res[i]+=tmp

            rightIdx=bisect_right(li,i)
            noOfItemsOnTheRight=len(li)-rightIdx
            rightSum=pre[-1]-pre[rightIdx]
            tmp=rightSum-i*noOfItemsOnTheRight
            res[i]+=tmp
        return res
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([4,2,7,2,4,4,5], get_sol().getDistances([2,1,3,1,2,3,3]))
    def test02(self):
        self.assertEqual([5,0,3,4], get_sol().getDistances([10,5,10,10]))
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
