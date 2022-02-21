from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution2()
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

class Solution2:
    # time: O(n) space: O(n)
    # leetcode original solution
    def findUnsortedSubarray(self, nums: List[int]) -> int:
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
        self.assertEqual(5,get_sol().findUnsortedSubarray([2,6,4,8,10,9,15]))
    def test2(self):
        self.assertEqual(2,get_sol().findUnsortedSubarray([3,1]))
    def test3(self):
        self.assertEqual(0,get_sol().findUnsortedSubarray([1,2,3,4]))
    def test4(self):
        self.assertEqual(0,get_sol().findUnsortedSubarray([1]))
    def test5(self):
        self.assertEqual(5,get_sol().findUnsortedSubarray([1,5,4,999,10,11]))
    def test6(self):
        self.assertEqual(9,get_sol().findUnsortedSubarray([1,3,4,7,6,2,12,10,9,11]))
