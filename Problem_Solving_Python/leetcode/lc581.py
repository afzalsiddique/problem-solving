from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class Solution:
    # time O(n) space constant
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Find right limit of the subarray. Traverse array from left to right
        right = None
        big = nums[0]
        for i in range(len(nums)):
            if nums[i] < big:
                # a number smaller than what we have seen -> need sorting
                right = i
            else:
                big = nums[i]

        # Find left limit of the subarray. Traverse array from right to left
        left = None
        small = nums[-1]
        for i in reversed(range(len(nums))):
            if nums[i] > small:
                # a number bigger than what we have seen -> need sorting
                left = i
            else:
                small = nums[i]

        if right == left: return 0
        return right - left + 1

    # time: O(n) space: O(n)
    # leetcode original solution
    def findUnsortedSubarray_(self, nums: List[int]) -> int:
        st=[]
        n=len(nums)
        left,right=n-1,0
        for i in range(n):
            idx=n-1
            while st and nums[st[-1]]>nums[i]:
                idx=st.pop()
            left=min(left,idx)
            st.append(i)
        st.clear()
        for i in reversed(range(n)):
            idx=0
            while st and nums[st[-1]]<nums[i]:
                idx=st.pop()
            right=max(right,idx)
            st.append(i)
        return right-left+1 if right>left else 0

class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(9,Solution().findUnsortedSubarray([1,3,4,7,6,2,12,10,9,11]))
    def test2(self):
        self.assertEqual(2,Solution().findUnsortedSubarray([3,1]))
    def test3(self):
        self.assertEqual(0,Solution().findUnsortedSubarray([1,2,3,4]))
    def test4(self):
        self.assertEqual(0,Solution().findUnsortedSubarray([1]))
