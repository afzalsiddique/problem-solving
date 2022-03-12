from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/wiggle-subsequence/discuss/84843/Easy-understanding-DP-solution-with-O(n)-Java-version/89522
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        up,down=1,1
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                down=up+1
            elif nums[i]>nums[i-1]:
                up=down+1
        return max(up,down)

class Solution2:
    # https://leetcode.com/problems/wiggle-subsequence/discuss/84843/Easy-understanding-DP-solution-with-O(n)-Java-version
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # dp[i][0] is the length of sequence ending at i and the last before element is lesser than last element. Eg. [9 2 5]
        # dp[i][1] is the length of sequence ending at i and the last before element is greater than last element. Eg. [2 10 5]
        n=len(nums)
        dp=[[1]*2 for _ in range(n)]
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                dp[i][0]=max(dp[i][0],1+dp[i-1][1])
                dp[i][1]=dp[i-1][1]
            elif nums[i]>nums[i-1]:
                dp[i][1]=max(dp[i][1],1+dp[i-1][0])
                dp[i][0]=dp[i-1][0]
            else:
                dp[i][1]=dp[i-1][1]
                dp[i][0]=dp[i-1][0]
        # return max(max(dp)) # this is wrong
        return max(map(max,dp))

class Solution3:
    # similar longest increasing subsequence
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # dp[i][0] is the length of sequence ending at i and the last before element is lesser than last element. Eg. [9 2 5]
        # dp[i][1] is the length of sequence ending at i and the last before element is greater than last element. Eg. [2 10 5]
        n=len(nums)
        dp=[[1]*2 for _ in range(n)]
        for i in range(1,n):
            for j in range(i):
                if nums[i]<nums[j]:
                    dp[i][0]=max(dp[i][0],1+dp[j][1])
                elif nums[i]>nums[j]:
                    dp[i][1]=max(dp[i][1],1+dp[j][0])
                else: # not necessary in this method but useful when doing it in O(n) time and O(n) space
                    dp[i][0]=max(dp[i][0],1)
                    dp[i][1]=max(dp[i][1],1)

        # return max(max(dp)) # this is wrong
        return max(map(max,dp))
class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(7,get_sol().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
    def test02(self):
        self.assertEqual(3,get_sol().wiggleMaxLength([3,3,3,2,5]))
    def test03(self):
        self.assertEqual(6,get_sol().wiggleMaxLength([1,7,4,9,2,5]))
    def test04(self):
        self.assertEqual(7,get_sol().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
    def test05(self):
        self.assertEqual(2,get_sol().wiggleMaxLength([1,2,3,4,5,6,7,8,9]))

