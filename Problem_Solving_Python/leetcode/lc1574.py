import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/discuss/830480/C%2B%2B-O(N)-Sliding-window-Explanation-with-Illustrations
    def findLengthOfShortestSubarray(self, A: List[int]) -> int:
        n=len(A)
        left=0
        right=n-1
        while left+1<n and A[left]<=A[left+1]:
            left+=1
        if left==n-1: return 0
        while right>left and A[right-1]<=A[right]:
            right-=1
        minn=min(n-left-1,right)
        i=0; j=right
        while i<=left and j<n:
            if A[i]<=A[j]:
                minn=min(minn,j-i-1)
                i+=1
            else:
                j+=1
        return minn


class MyTestCase(unittest.TestCase):
    def test_1(self):
        arr = [1,2,3,10,4,2,3,5]
        Output= 3
        self.assertEqual(Output, get_sol().findLengthOfShortestSubarray(arr))
    def test_2(self):
        arr = [5,4,3,2,1]
        Output= 4
        self.assertEqual(Output, get_sol().findLengthOfShortestSubarray(arr))
    def test_3(self):
        arr = [1,2,3]
        Output= 0
        self.assertEqual(Output, get_sol().findLengthOfShortestSubarray(arr))
    def test_4(self):
        arr = [1]
        Output= 0
        self.assertEqual(Output, get_sol().findLengthOfShortestSubarray(arr))
    def test_5(self):
        arr = [2,2,2,1,1,1]
        Output= 3
        self.assertEqual(Output, get_sol().findLengthOfShortestSubarray(arr))
    def test_6(self):
        arr = [6,3,10,11,15,20,13,3,18,12]
        Output= 8
        self.assertEqual(Output, get_sol().findLengthOfShortestSubarray(arr))
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
