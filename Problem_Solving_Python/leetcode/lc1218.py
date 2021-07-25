import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # Let dp[i] be the maximum length of a subsequence of the given difference whose last element is i.
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        di=defaultdict(int)
        for x in arr:
            di[x]=max(di[x],di[x-diff]+1)
        return max(di.values())
class Solution2:
    # tle
    # longest increasing subsequence template
    # Let dp[i] be the maximum length of a subsequence of the given difference whose last element is i.
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        n=len(arr)
        dp=[1]*n
        for i in range(n):
            for j in range(i):
                if arr[j]+diff==arr[i]:
                    dp[i]=max(dp[i],dp[j]+1)
        # print(dp)
        return max(dp)
class tester(unittest.TestCase):
    def test_1(self):
        arr = [1,2,3,4]
        diff = 1
        Output= 4
        self.assertEqual(Output, get_sol().longestSubsequence(arr,diff))
    def test_2(self):
        arr = [1,3,5,7]
        diff = 1
        Output= 1
        self.assertEqual(Output, get_sol().longestSubsequence(arr,diff))
    def test_3(self):
        arr = [1,5,7,8,5,3,4,2,1]
        diff = -2
        Output= 4
        self.assertEqual(Output, get_sol().longestSubsequence(arr,diff))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):