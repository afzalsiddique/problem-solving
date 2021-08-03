import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n=len(arr)
        cur_sum=0
        for i in range(k-1):
            cur_sum+=arr[i]

        cnt=0
        for i in range(k-1,n):
            cur_sum+=arr[i]
            if cur_sum//k>=threshold: cnt+=1
            cur_sum-=arr[i-k+1]
        return cnt
class Tester(unittest.TestCase):
    def test1(self):
        arr,k,threshold= [2,2,2,2,5,5,5,8], 3,  4
        Output= 3
        self.assertEqual(Output,get_sol().numOfSubarrays(arr,k,threshold))
    def test2(self):
        arr,k,threshold= [1,1,1,1,1], 1,  0
        Output= 5
        self.assertEqual(Output,get_sol().numOfSubarrays(arr,k,threshold))
    def test3(self):
        arr,k,threshold= [11,13,17,23,29,31,7,5,2,3], 3,  5
        Output= 6
        self.assertEqual(Output,get_sol().numOfSubarrays(arr,k,threshold))
    def test4(self):
        arr,k,threshold= [7,7,7,7,7,7,7], 7,  7
        Output= 1
        self.assertEqual(Output,get_sol().numOfSubarrays(arr,k,threshold))
    def test5(self):
        arr,k,threshold= [4,4,4,4], 4,  1
        Output= 1
        self.assertEqual(Output,get_sol().numOfSubarrays(arr,k,threshold))
    # def test6(self):
    # def test7(self):