import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n=len(nums)
        flipped = [False]*n
        validFlipTimesFromPastWindowKForCurrentIdx = 0 # no of flips done to the current index from previous flips
        res =0
        for i in range(n):
            if i>=k:
                if flipped[i-k]:
                    validFlipTimesFromPastWindowKForCurrentIdx-=1

            if validFlipTimesFromPastWindowKForCurrentIdx%2 == nums[i]:
                if i+k>n:
                    return -1
                validFlipTimesFromPastWindowKForCurrentIdx+=1
                flipped[i]=True
                res+=1

        return res
class Solution2:
    # https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/discuss/239284/C%2B%2B-greedy-stack-and-O(1)-memory
    # time O(n) space O(k)
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n=len(nums)
        q=deque()
        res=0
        for i in range(n): # this window = [min(0,i-k+1):i+1]
            if q and q[0]<i: # remove expired flip to this window
                q.popleft()
            noOfFlipsDoneToTheCurrentIdx=len(q) # len(q) denotes no of flips done to the current index from previous flips
            if nums[i]==noOfFlipsDoneToTheCurrentIdx%2:
                res+=1
                if i+k-1>=n: return -1
                q.append(i+k-1) # put end index of the window where the flip is applicable
        return res
class Solution3:
    # tle
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n=len(nums)
        target=2**n-1
        mask = ''.join(str(x) for x in nums)
        mask=int(mask,2)
        q=deque([mask])
        vis= {mask}
        res=0
        while q:
            for _ in range(len(q)):
                mask=q.popleft()
                if mask==target: return res
                for i in range(n-k+1):
                    x=2**k-1<<i
                    new_mask=mask^x
                    if new_mask not in vis:
                        vis.add(new_mask)
                        q.append(new_mask)
            res+=1
        return -1

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, get_sol().minKBitFlips(nums = [0,1,0], k = 1))
    def test2(self):
        self.assertEqual(-1, get_sol().minKBitFlips(nums = [1,1,0], k = 2))
    def test3(self):
        self.assertEqual(3, get_sol().minKBitFlips(nums = [0,0,0,1,0,1,1,0], k = 3))
    def test4(self):
        self.assertEqual(17, get_sol().minKBitFlips([1,1,1,1,1,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,0,1,1,1,0,0,0,0,1,1,1], 8))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):
    # def test7(self):
    # def test8(self):
