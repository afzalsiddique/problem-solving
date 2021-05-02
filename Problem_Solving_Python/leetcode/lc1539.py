import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
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


class tester(unittest.TestCase):
    def test1(self):
        arr = [2,3,4,7,11]
        k = 5
        Output= 9
        self.assertEqual(Output,Solution().findKthPositive(arr,k))
    def test2(self):
        arr = [1,2,3,4]
        k = 2
        Output= 6
        self.assertEqual(Output,Solution().findKthPositive(arr,k))
    def test3(self):
        arr = [2]
        k = 1
        Output= 1
        self.assertEqual(Output,Solution().findKthPositive(arr,k))
