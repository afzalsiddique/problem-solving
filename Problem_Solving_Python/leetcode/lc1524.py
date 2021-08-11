import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
# similar 1567
class Solution:
    # see array version for visualization below
    # time O(n) space O(1)
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD=10**9+7; n=len(arr)
        summ=0
        if arr[0]%2:
            odd=1
            even=0
        else:
            odd=0
            even=1
        summ+=odd
        for i in range(1,n):
            prev_odd=odd
            prev_even=even
            if arr[i]%2:
                odd=prev_even+1
                even=prev_odd
            else:
                odd=prev_odd
                even=prev_even+1
            summ+=odd
        return summ % MOD
class Solution2:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD=10**9+7; n=len(arr)
        odd=[]
        even=[]
        if arr[0]%2:
            odd.append(1)
            even.append(0)
        else:
            odd.append(0)
            even.append(1)
        for i in range(1,n):
            if arr[i]%2:
                odd.append(even[i-1]+1)
                even.append(odd[i-1])
            else:
                odd.append(odd[i-1])
                even.append(even[i-1]+1)
        # print(odd)
        # print(even)
        return sum(odd) % MOD

class MyTestCase(unittest.TestCase):
    def test_1(self):
        arr = [1,3,5]
        Output= 4
        self.assertEqual(Output, get_sol().numOfSubarrays(arr))
    def test_2(self):
        arr = [2,4,6]
        Output= 0
        self.assertEqual(Output, get_sol().numOfSubarrays(arr))
    def test_3(self):
        arr = [1,2,3,4,5,6,7]
        Output= 16
        self.assertEqual(Output, get_sol().numOfSubarrays(arr))
    def test_4(self):
        arr = [100,100,99,99]
        Output= 4
        self.assertEqual(Output, get_sol().numOfSubarrays(arr))
    def test_5(self):
        arr = [7]
        Output= 1
        self.assertEqual(Output, get_sol().numOfSubarrays(arr))
    # def test_6(self):