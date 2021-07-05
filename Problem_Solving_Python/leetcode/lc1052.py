import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], window: int) -> int:
        n=len(customers)
        maxx=float('-inf')
        tmp=0
        for i in range(window-1):
            if grumpy[i]: tmp+=customers[i]
        for i in range(window-1, n):
            if grumpy[i]: tmp+=customers[i]
            maxx=max(maxx,tmp)
            window_beginning=i-window+1
            if grumpy[window_beginning]: tmp-=customers[window_beginning]

        summ=0
        for i in range(n):
            if not grumpy[i]: summ+=customers[i]
        return summ+maxx
class Solution2:
    # tle
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n=len(customers)
        maxx=float('-inf')
        for i in range(n-minutes+1):
            tmp=0
            for j in range(minutes):
                if grumpy[i+j]: tmp+=customers[i+j]
            if tmp>maxx:
                maxx=tmp
        summ=0
        for i in range(n):
            if not grumpy[i]: summ+=customers[i]
        # print(maxx,summ)
        return summ+maxx

class MyTestCase(unittest.TestCase):
    def test_01(self):
        customers = [1,0,1,2,1,1,7,5]
        grumpy =    [0,1,0,1,0,1,0,1]
        minutes = 3
        Output=16
        self.assertEqual(Output,get_sol().maxSatisfied(customers,grumpy,minutes))
    def test_02(self):
        customers = [4,10,10]
        grumpy =    [1,1,0]
        minutes = 2
        Output=24
        self.assertEqual(Output,get_sol().maxSatisfied(customers,grumpy,minutes))



# def test_03(self):
# def test_04(self):
