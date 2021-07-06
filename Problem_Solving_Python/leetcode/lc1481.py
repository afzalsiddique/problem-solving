import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # similar to 1338
    # similar to bucket sort
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        freq = [0]*(len(arr)+1)
        for x in count:
            freq[count[x]]+=1
        for i in range(len(freq)):
            while freq[i]!=0 and k>=i:
                k-=i
                freq[i]-=1
        return sum(freq)

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
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):