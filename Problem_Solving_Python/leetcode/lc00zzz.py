from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        def f(left, cnt):
            nonlocal res
            if left==0:
                res=max(res, cnt, key=lambda x:sum(x.values()))
                return
            if left<0:
                return
            for num in cost.keys():
                cnt2=Counter({k:v for k,v in cnt.items()})
                cnt2[num]+=1
                f(left-cost[num],cnt2)
            return


        sett=set()
        costDi={}
        for i in range(9-1,-1,-1):
            num=i+1
            if cost[i] not in sett:
                costDi[num]=cost[i]
                sett.add(cost[i])
        cost=costDi

        res=Counter({i:0 for i in range(1,9+1)})
        # nums=sorted(cost.keys(),reverse=True)
        f(target,Counter({i:0 for i in range(1,9+1)}))
        print(res)
        res=''.join(map(str,res))
        return '0' if res=='' else res





class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual("7772", get_sol().largestNumber([4,3,2,5,6,7,2,5,5], 9))
    def test2(self):
        self.assertEqual("85", get_sol().largestNumber( [7,6,5,5,5,6,8,7,8], 12))
    def test3(self):
        self.assertEqual("0", get_sol().largestNumber([2,4,6,2,4,6,4,4,4], 5))
    def test4(self):
        self.assertEqual("0", get_sol().largestNumber([210,77,91,105,1208,511,3392,3029,1029], 4031))
    def test5(self):
        self.assertEqual("87432222222222222222222222222222222222222222222", get_sol().largestNumber([210,77,91,105,1908,3953,530,410,1237], 4447))
    def test6(self):
        self.assertEqual("5555443222", get_sol().largestNumber([1000,30,105,70,42,1000,1000,1000,1000], 503))
    # def test7(self):
    # def test8(self):
