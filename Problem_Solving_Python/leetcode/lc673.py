from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import cache; from heapq import *; import unittest; from typing import List, Optional; import functools;from sortedcontainers import SortedList
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # length[i]: the length of the Longest Increasing Subsequence which ends with nums[i].
    # cnt[i]   : the number of the Longest Increasing Subsequence which ends with nums[i].
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        length=[1]*n
        cnt=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if length[i]<length[j]+1:
                        length[i]=length[j]+1
                        cnt[i]=cnt[j]
                    elif length[i]==length[j]+1:
                        cnt[i]+=cnt[j]

        max_len=max(length)
        return sum(cnt[i] for i in range(n) if length[i]==max_len)
class Solution2:
    # length[i]: the length of the Longest Increasing Subsequence which ends with nums[i].
    # cnt[i]   : the number of the Longest Increasing Subsequence which ends with nums[i].
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        length=[1]*n
        cnt=[1]*n
        max_len=0
        res=0
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if length[i]<length[j]+1:
                        length[i]=length[j]+1
                        cnt[i]=cnt[j]
                    elif length[i]==length[j]+1:
                        cnt[i]+=cnt[j]
            if max_len<length[i]:
                max_len=length[i]
                res = cnt[i]
            elif max_len==length[i]:
                res+=cnt[i]
        return res


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(2, get_sol().findNumberOfLIS([1,3,5,4,7]))
    def test02(self):
        self.assertEqual(5, get_sol().findNumberOfLIS([2,2,2,2,2]))
    def test03(self):
        self.assertEqual(3, get_sol().findNumberOfLIS([4,3,5,4,7,2]))
    def test04(self):
        self.assertEqual(3, get_sol().findNumberOfLIS([1,2,4,3,5,4,7,2]))
    def test05(self):
        self.assertEqual(18, get_sol().findNumberOfLIS([1,5,4,3,8,7,6,10,9])) # run this example to understand the code
    def test06(self):
        self.assertEqual(1, get_sol().findNumberOfLIS([10,9,8,7,6,5,6,7,8,9,10]))
    def test07(self):
        self.assertEqual(1, get_sol().findNumberOfLIS([6,5,6,7]))
