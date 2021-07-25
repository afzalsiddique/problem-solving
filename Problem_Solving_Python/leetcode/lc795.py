import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/discuss/117723/Python-standard-DP-solution-with-explanation/977773
    def numSubarrayBoundedMax(self, A: List[int], l: int, r: int) -> int:
        res=0
        #  dp[i] denotes the max number of valid sub-array ending with A[i].
        # dp=[0]*len(A) # could be replaced by a variable cnt
        prev = -1 # previous index of A[i] > R
        cnt=0
        for i in range(len(A)):
            if A[i] > r:
                cnt = 0
                prev = i
            elif A[i]>=l:
                cnt = i - prev
            res += cnt
            # dp[i]=cnt
        # print(dp)
        return res
class Solution2:
    # https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/discuss/1278624/Python-simple-O(n)-solution-explained
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        L_ind, R_ind, ans = -1, -1, 0
        for i, num in enumerate(A):
            if num >= L: L_ind = i
            if num > R:  R_ind = i
            ans += L_ind - R_ind
        return ans
class Solution3:
    # wrong
    def numSubarrayBoundedMax(self, A: List[int], l: int, r: int) -> int:
        #  dp[i] denotes the max number of valid sub-array ending with A[i].
        # dp=[0] * len(A)
        res=0
        cnt=0
        for i in range(len(A)):
            if A[i] > r:
                cnt = 0
            if A[i]>=l:
                cnt+=1
            res += cnt
            # dp[i]=cnt
        # print(dp)
        return res
class tester(unittest.TestCase):
    def test_1(self):
        nums = [2,1,4,3]
        left = 2
        right = 3
        Output= 3
        self.assertEqual(Output, get_sol().numSubarrayBoundedMax(nums,left,right))
    def test_2(self):
        nums = [2,9,2,5,6]
        left = 2
        right = 8
        Output= 7
        self.assertEqual(Output, get_sol().numSubarrayBoundedMax(nums,left,right))
    def test_3(self):
        nums = [73,55,36,5,55,14,9,7,72,52]
        left = 32
        right = 69
        Output= 22
        self.assertEqual(Output, get_sol().numSubarrayBoundedMax(nums,left,right))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):