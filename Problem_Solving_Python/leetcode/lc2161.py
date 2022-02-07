from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def getTime(time):
            li = []
            if time<100:
                li.append(str(time))
            min=time//60
            secs=time%60
            if min<100:
                if secs<10:
                    li.append(str(min)+'0'+str(secs))
                else:
                    li.append(str(min)+str(secs))
            if secs<=39:
                li.append(str(min-1)+str(secs+60))
            return li

        def calculate(time):
            n=len(time)
            cur=str(startAt)
            res=0
            i=0
            while i<n:
                if cur!=time[i]:
                    cur=time[i]
                    res+=moveCost
                res+=pushCost
                i+=1
            return res

        li = getTime(targetSeconds)
        # print(li)
        minn=float('inf')
        for x in li:
            minn=min(minn,calculate(x))
        return minn


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(6, get_sol().minCostSetTime(1, 2, 1, 600))
    def test02(self):
        self.assertEqual(6, get_sol().minCostSetTime(0, 1, 2, 76))
    def test03(self):
        self.assertEqual(4, get_sol().minCostSetTime(9, 100000, 1, 6039))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
