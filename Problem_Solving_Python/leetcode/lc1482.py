from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def minDays(self, bloomDay: List[int], min_bouquets: int, flowers_per_bouquet: int) -> int:
        def feasible(days) -> bool:
            bouquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom > days: # if not adjacent
                    flowers = 0
                else:
                    flowers+=1
                    if flowers==flowers_per_bouquet:
                        bouquets+=1
                        flowers=0

                    # flowers+=1
                    # bouquets += flowers // flowers_per_bouquet
                    # flowers = flowers % flowers_per_bouquet

            return bouquets >= min_bouquets

        if len(bloomDay) < min_bouquets * flowers_per_bouquet:
            return -1
        left, right = 1, max(bloomDay)
        while left <= right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left



class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(3,get_sol().minDays([1,10,3,10,2],3,1))
    def test02(self):
        self.assertEqual(-1,get_sol().minDays([1,10,3,10,2],3,2))
    def test03(self):
        self.assertEqual(12,get_sol().minDays([7,7,7,7,12,7,7],2,3))
    def test04(self):
        self.assertEqual(9,get_sol().minDays([1,10,2,9,3,8,4,7,5,6], 4, 2))

