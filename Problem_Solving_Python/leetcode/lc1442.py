import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # time O(n^2) space O(n)
    # if a==b then a^b=0
    def countTriplets(self, arr: List[int]) -> int:
        def get_xor(i,j): return pre_xor[j]^pre_xor[i]^arr[i]
        n=len(arr)
        pre_xor=list(itertools.accumulate(arr,lambda a,b: a^b))
        cnt=0
        for i in range(n):
            for k in range(i+1,n):
                a=get_xor(i,k)
                if a==0:
                    # [14,-2,-3,-4,-5]
                    # 1. [14]+[-2,-3,-4,-5] =0
                    # 2. [14,-2]+[-3,-4,-5] =0
                    # 3. [14,-2,-3]+[-4,-5] =0
                    # 4. [14,-2,-3,-4]+[-5] =0
                    # (k-i+1)-1 ways to make it equal to 0
                    cnt+=k-i
        return cnt

class Tester(unittest.TestCase):
    def test1(self):
        arr = [2,3,1]
        Output= 4
        self.assertEqual(Output,get_sol().countTriplets(arr))
    def test2(self):
        arr = [1,1,1,1,1]
        Output= 10
        self.assertEqual(Output,get_sol().countTriplets(arr))
    def test3(self):
        arr = [2,3]
        Output= 0
        self.assertEqual(Output,get_sol().countTriplets(arr))
    def test4(self):
        arr = [1,3,5,7,9]
        Output= 3
        self.assertEqual(Output,get_sol().countTriplets(arr))
    def test5(self):
        arr = [7,11,12,9,5,2,7,17,22]
        Output= 8
        self.assertEqual(Output,get_sol().countTriplets(arr))
    # def test6(self):
    # def test7(self):
