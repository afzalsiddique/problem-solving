import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/discuss/377397/Intuitive-Java-Solution-With-Explanation
    def kadanes(self,A:List[int]):
        n=len(A)
        max_ending_here=[0]*n
        max_ending_here[0]=A[0]
        for i in range(1,n):
            max_ending_here[i]=max(A[i], max_ending_here[i - 1] + A[i])
        return max_ending_here
    def maximumSum(self, A: List[int]) -> int:
        n=len(A)
        max_ending_here=self.kadanes(A)
        max_starting_here=self.kadanes(A[::-1])[::-1]
        res=float('-inf')
        for i in range(n-2):
            res=max(res,max_ending_here[i]+max_starting_here[i+2])
        return max(res,max(max_ending_here),max(max_starting_here))
class Solution2:
    # https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/discuss/377397/Intuitive-Java-Solution-With-Explanation
    def maximumSum(self, A: List[int]) -> int:
        n=len(A)
        max_ending_here=[0]*n
        max_ending_here[0]=A[0]
        for i in range(1,n):
            max_ending_here[i]=max(A[i], max_ending_here[i - 1] + A[i])

        max_starting_here=[0]*n
        max_starting_here[n-1]=A[n - 1]
        for i in range(n-2,-1,-1):
            max_starting_here[i]=max(A[i], max_starting_here[i + 1] + A[i])

        res=float('-inf')
        for i in range(n-2):
            res=max(res,max_ending_here[i]+max_starting_here[i+2])
        return max(res,max(max_ending_here),max(max_starting_here))

class MyTestCase(unittest.TestCase):
    def test01(self):
        arr = [1,-2,0,3]
        Output= 4
        self.assertEqual(Output,get_sol().maximumSum(arr))
    def test02(self):
        arr = [1,-2,-2,3]
        Output= 3
        self.assertEqual(Output,get_sol().maximumSum(arr))
    def test03(self):
        arr = [-1,-1,-1,-1]
        Output= -1
        self.assertEqual(Output,get_sol().maximumSum(arr))
    def test04(self):
        self.assertEqual(-50,get_sol().maximumSum([-50]))
    # def test_5(self):
    # def test_6(self):
