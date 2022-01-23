from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # index based. useful in "nextGreaterElement-ii".
        nxt,st = [-1]*len(nums2),[]
        for i in range(len(nums2)):
            while st and nums2[i]>=nums2[st[-1]]:
                top = st.pop()
                nxt[top] = nums2[i]
            st.append(i)
        index={}
        for i,num in enumerate(nums2):
            index[num]=i
        next_greater = []
        for num in nums1:
            next_greater.append(nxt[index[num]])
        return next_greater

        # element based
        st,di,nxt=[],{},[]
        for num in nums2:
            while st and num>st[-1]:
                top = st.pop()
                di[top] = num
            st.append(num)
        for num in nums1:
            if num in di:
                nxt.append(di[num])
            else:
                nxt.append(-1)
        return nxt

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual([-1,12,12,-1,-1], get_sol().nextGreaterElement([13,7,6,12,10],[13,7,6,12,10]))
    def test_2(self):
        self.assertEqual([3,-1], get_sol().nextGreaterElement( nums1 = [2,4], nums2 = [1,2,3,4]))
    def test_3(self):
        self.assertEqual([-1,3,-1], get_sol().nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))