from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=88k8xa-pSrM
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def compute(actual,expected):
            return actual - expected

        lo=0
        hi=len(arr)-1
        while lo<=hi:
            mid=(lo+hi)//2
            missing = compute(arr[mid],mid+1)
            if missing>=k:
                hi=mid-1
            else:
                lo=mid+1
        if hi==-1: return k
        return arr[hi]+k-compute(arr[hi],hi+1)

class Solution2:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=0
        missing=1
        while k and i<len(arr):
            if arr[i]==missing:
                i+=1
                missing+=1
            elif arr[i]>missing:
                k-=1
                missing+=1
        while k:
            missing+=1
            k-=1
        return missing-1
class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(9,get_sol().findKthPositive([2,3,4,7,11],5))
    def test02(self):
        self.assertEqual(6,get_sol().findKthPositive([1,2,3,4],2))
    def test03(self):
        self.assertEqual(1,get_sol().findKthPositive([2],1))
