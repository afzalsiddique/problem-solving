from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def minEatingSpeed(self, A: List[int], h: int) -> int:
        def canEatAll(speed):
            # return sum(ceil(a/speed) for a in A)<=h # one liner
            time=0
            for a in A:
                time+=ceil(a/speed)
            return time<=h

        lo,hi=1,max(A)
        while lo<=hi:
            m=(lo+hi)//2
            if canEatAll(m):
                hi=m-1
            else:
                lo=m+1
        return lo
class Solution2:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_all(k):
            cnt=0
            for pile in piles:
                if pile%k:
                    cnt+=pile//k+1
                else:
                    cnt+=pile//k
            return cnt<=h

        lo=1
        hi = max(piles)
        while lo<=hi:
            mid = (lo+hi)//2
            if can_eat_all(mid):
                hi=mid-1
            else:
                lo=mid+1
        return lo



class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(4,get_sol().minEatingSpeed([3,6,7,11],8))
    def test02(self):
        self.assertEqual(30,get_sol().minEatingSpeed([30,11,23,4,20],5))
    def test03(self):
        self.assertEqual(23,get_sol().minEatingSpeed([30,11,23,4,20],6))
    def test04(self):
        self.assertEqual(1,get_sol().minEatingSpeed([312884470],968709470))