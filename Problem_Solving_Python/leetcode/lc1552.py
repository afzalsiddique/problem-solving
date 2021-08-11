import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def count(d):
            res=1
            prev=0
            # li=[position[0]] # for visualization
            for i in range(1,n):
                if position[i]-position[prev]>=d:
                    prev=i
                    res+=1
                    # li.append(position[i]) # for visualization
            return res

        n=len(position)
        position.sort()
        i_lo=0; i_hi=10**11
        while i_lo<=i_hi:
            mid=(i_lo+i_hi)//2
            ans=count(mid)
            # if ans==m: return mid
            if ans>=m:
                i_lo=mid+1
            else:
                i_hi=mid-1
        return i_lo-1


class MyTestCase(unittest.TestCase):
    def test_1(self):
        position,m = [1,2,3,4,7], 3
        Output= 3
        self.assertEqual(Output, get_sol().maxDistance(position,m))
    def test_2(self):
        position,m = [1,2,3,4,5,6,7,8,9], 3
        Output= 4
        self.assertEqual(Output, get_sol().maxDistance(position,m))
    def test_3(self):
        position,m = [5,4,3,2,1,1000000000], 2
        Output= 999999999
        self.assertEqual(Output, get_sol().maxDistance(position,m))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):