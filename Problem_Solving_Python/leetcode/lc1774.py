import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        m=len(toppingCosts)
        di=Counter()
        sett=set()
        def valid():
            for k in di:
                if di[k]>2: return False
            return True
        def h(start, summ):
            if not valid():
                return
            if summ>target+maxx:
                return
            sett.add(summ)
            for i in range(start,m):
                h(i + 1, summ)

                di[i]+=1
                h(i + 1, summ + toppingCosts[i])
                di[i]-=1

                di[i]+=2
                h(i + 1, summ + 2*toppingCosts[i])
                di[i]-=2

        maxx=max(max(toppingCosts),max(baseCosts))
        h(0,0)
        # print(sett)
        minn_cost=float('inf')
        minn_diff=float('inf')
        for tops in sett:
            for base in baseCosts:
                cost=tops+base
                diff=abs(target-cost)
                if diff<=minn_diff:
                    if diff==minn_diff:
                        minn_cost=min(minn_cost,cost)
                    else:
                        minn_cost=cost
                    minn_diff=diff
        return minn_cost




class MyTestCase(unittest.TestCase):
    def test_1(self):
        baseCosts,toppingCosts,target = [1,7],[3,4], 10
        Output= 10
        self.assertEqual(Output, get_sol().closestCost(baseCosts,toppingCosts,target))
    def test_2(self):
        baseCosts,toppingCosts,target = [2,3],[4,5,100], 18
        Output= 17
        self.assertEqual(Output, get_sol().closestCost(baseCosts,toppingCosts,target))
    def test_3(self):
        baseCosts,toppingCosts,target = [3,10],[2,5], 9
        Output= 8
        self.assertEqual(Output, get_sol().closestCost(baseCosts,toppingCosts,target))
    def test_4(self):
        baseCosts,toppingCosts,target = [10],[1], 1
        Output= 10
        self.assertEqual(Output, get_sol().closestCost(baseCosts,toppingCosts,target))
    def test_5(self):
        baseCosts,toppingCosts,target = [10,1,10], [7,5,1,1,1], 5
        Output= 5
        self.assertEqual(Output, get_sol().closestCost(baseCosts,toppingCosts,target))
    def test_6(self):
        baseCosts,toppingCosts,target = [6377,9493,6978,6640,5506,9576], [1110,8073,4058,4766,341,6669,2558,6510,4428,2919], 1203
        Output= 5506
        self.assertEqual(Output, get_sol().closestCost(baseCosts,toppingCosts,target))
    def test_7(self):
        baseCosts,toppingCosts,target = [3738,5646,197,7652],[5056], 9853
        Output= 10309
        self.assertEqual(Output, get_sol().closestCost(baseCosts,toppingCosts,target))
    def test_8(self):
        baseCosts,toppingCosts,target = [1], [6,5012], 5001
        Output= 5013
        self.assertEqual(Output, get_sol().closestCost(baseCosts,toppingCosts,target))
    # def test_9(self):