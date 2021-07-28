import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/discuss/377397/Intuitive-Java-Solution-With-Explanation
    def maximumSum(self, arr: List[int]) -> int:
        n=len(arr)
        max_ending_here=[0]*n
        max_ending_here[0]=arr[0]
        for i in range(1,n):
            max_ending_here[i]=max(arr[i], max_ending_here[i - 1] + arr[i])

        max_starting_here=[0]*n
        max_starting_here[n-1]=arr[n - 1]
        for i in range(n-2,-1,-1):
            max_starting_here[i]=max(arr[i], max_starting_here[i + 1] + arr[i])

        res=float('-inf')
        for i in range(n-2):
            res=max(res,max_ending_here[i]+max_starting_here[i+2])
        return max(res,max(max_ending_here),max(max_starting_here))

class MyTestCase(unittest.TestCase):
    def test_1(self):
        arr = [1,-2,0,3]
        Output= 4
        self.assertEqual(Output,get_sol().maximumSum(arr))
    def test_2(self):
        arr = [1,-2,-2,3]
        Output= 3
        self.assertEqual(Output,get_sol().maximumSum(arr))
    def test_3(self):
        arr = [-1,-1,-1,-1]
        Output= -1
        self.assertEqual(Output,get_sol().maximumSum(arr))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):