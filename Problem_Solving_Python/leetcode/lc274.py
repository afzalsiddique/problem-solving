from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def valid(hVal):
            cnt=0
            for c in citations:
                if c>=hVal:
                    cnt+=1
            return cnt >= hVal
        lo,hi=0,max(citations)
        while lo<=hi:
            m=(lo+hi)//2
            if valid(m):
                lo=m+1
            else:
                hi=m-1
        return lo-1
        # return hi
class Solution2:
    # counting sort
    # https://leetcode.com/problems/h-index/discuss/70768/Java-bucket-sort-O(n)-solution-with-detail-explanation
    def hIndex(self, citations):
        n = len(citations)
        buckets = [0 for _ in range(n + 1)]

        for num in citations:
            if num >= n:
                buckets[n] += 1
            else:
                buckets[num] += 1

        count = 0

        for i in reversed(range(len(buckets))):
            count += buckets[i]

            if count >= i:
                return i

        return 0
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(3, get_sol().hIndex( [3,0,6,1,5]))
    def test02(self):
        self.assertEqual(1, get_sol().hIndex([1,3,1]))
