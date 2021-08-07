import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD=10**9+7
        def max_subarray_sum(arr):
            n=len(arr)
            max_ending_here=[0]*n
            max_ending_here[0]=max(0,arr[0])
            for i in range(1,n):
                max_ending_here[i]=max(arr[i],arr[i]+max_ending_here[i-1])
            return max(max_ending_here)
        def max_pre(arr): # max_prefix_sum
            n=len(arr)
            max_pre=0
            cur=0
            for i in range(n):
                cur+=arr[i]
                max_pre=max(max_pre,cur)
            return max_pre
        def max_suf(arr): # max_suffix_sum
            n=len(arr)
            max_post=0
            cur=0
            for i in reversed(range(n)):
                cur+=arr[i]
                max_post=max(max_post,cur)
            return max_post

        if k==1: return max_subarray_sum(arr) % MOD
        summ=sum(arr)
        maxx=max(0,summ*k)
        maxx=max(maxx,max_subarray_sum(arr+arr))
        maxx=max(maxx,max_suf(arr)+summ*(k-2)+max_pre(arr))
        return maxx % MOD

class Tester(unittest.TestCase):
    def test_1(self):
        arr,k = [1,2],3
        Output= 9
        self.assertEqual(Output,get_sol().kConcatenationMaxSum(arr,k))
    def test_2(self):
        arr,k = [1,-2,1],5
        Output= 2
        self.assertEqual(Output,get_sol().kConcatenationMaxSum(arr,k))
    def test_3(self):
        arr,k = [-1,-2],7
        Output= 0
        self.assertEqual(Output,get_sol().kConcatenationMaxSum(arr,k))
    def test_4(self):
        arr,k = [1,2], 1
        Output= 3
        self.assertEqual(Output,get_sol().kConcatenationMaxSum(arr,k))
    def test_5(self):
        arr,k = [-5,-2,0,0,3,9,-2,-5,4], 5
        Output= 20
        self.assertEqual(Output,get_sol().kConcatenationMaxSum(arr,k))
    def test_6(self):
        arr,k = [-5,4,-4,-3,5,-3], 3
        Output= 5
        self.assertEqual(Output,get_sol().kConcatenationMaxSum(arr,k))
    def test_7(self):
        arr,k = [10000,10000,10000,10000,10000,10000,10000,10000,10000,10000], 100000
        Output= 999999937
        self.assertEqual(Output,get_sol().kConcatenationMaxSum(arr,k))
    def test_8(self):
        # MAX SUB ARRAY SUM OF ARR+ARR
        arr,k = [-9,13,4,-16,-12,-16,3,-7,5,-16,16,8,-1,-13,15,3], 6
        Output= 36
        self.assertEqual(Output,get_sol().kConcatenationMaxSum(arr,k))
