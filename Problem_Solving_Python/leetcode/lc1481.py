import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    # frequency buckets
    # similar to 1338
    # similar to bucket sort
    # time O(n) space O(n)
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        n=len(arr)
        freq=defaultdict(int)
        for a in arr: freq[a]+=1
        freq_buckets=[0]*(n+1)
        for cnt in freq.values():
            freq_buckets[cnt]+=1
        i=0
        while i<=n and k>0:
            while freq_buckets[i]!=0 and k>=i:
                freq_buckets[i]-=1
                k-=i
            i+=1
        return sum(freq_buckets)

class tester(unittest.TestCase):
    def test_1(self):
        arr = [5,5,4]
        k = 1
        Output= 1
        self.assertEqual(Output,get_sol().findLeastNumOfUniqueInts(arr,k))
    def test_2(self):
        arr = [4,3,1,1,3,3,2]
        k = 3
        Output= 2
        self.assertEqual(Output,get_sol().findLeastNumOfUniqueInts(arr,k))
    def test_3(self):
        self.assertEqual(0,get_sol().findLeastNumOfUniqueInts([1],1))

    # def test_4(self):
    # def test_5(self):
    # def test_6(self):