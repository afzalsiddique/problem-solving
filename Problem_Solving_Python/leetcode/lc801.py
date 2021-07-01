import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # time O(n) space O(1)
    # https://www.youtube.com/watch?v=mLTF2UXkd2o
    # https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/discuss/119879/JavaC%2B%2BPython-DP-O(N)-Solution
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n=len(A)

        fixed=0
        swap=1
        for i in range(1,n):
            swap2=fixed2=float('inf')
            if A[i]>A[i-1] and B[i]>B[i-1]:
                fixed2=fixed
                swap2=swap+1
            if A[i]>B[i-1] and B[i]>A[i-1]:
                fixed2=min(fixed2,swap)
                swap2=min(swap2,fixed+1)
            swap,fixed=swap2,fixed2
        # print(fixed)
        # print(swap)

        return min(swap,fixed)
class Solution2:
    # time O(n) space O(n)
    # https://www.youtube.com/watch?v=mLTF2UXkd2o
    # https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/discuss/119879/JavaC%2B%2BPython-DP-O(N)-Solution
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n=len(A)
        fixed=[n]*n
        swap=[n]*n

        fixed[0]=0
        swap[0]=1
        for i in range(1,n):
            if A[i]>A[i-1] and B[i]>B[i-1]:
                fixed[i]=fixed[i-1]
                swap[i]=swap[i-1]+1
            if A[i]>B[i-1] and B[i]>A[i-1]:
                fixed[i]=min(fixed[i],swap[i-1])
                swap[i]=min(swap[i],fixed[i-1]+1)
        # print(fixed)
        # print(swap)

        return min(swap[-1],fixed[-1])


class tester(unittest.TestCase):
    def test01(self):
        nums1 = [1,3,5,4]
        nums2 = [1,2,3,7]
        Output= 1
        self.assertEqual(Output,get_sol().minSwap(nums1,nums2))
    def test02(self):
        nums1 = [0,3,5,8,9]
        nums2 = [2,1,4,6,9]
        Output= 1
        self.assertEqual(Output,get_sol().minSwap(nums1,nums2))
    # def test03(self):
