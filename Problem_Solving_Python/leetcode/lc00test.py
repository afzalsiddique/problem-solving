from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional,Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
class Solution:
    def largest_arr(self, nums, k):
        n=len(nums)
        st=[]
        for i,x in enumerate(nums):
            if i<n-k+len(st):
                if not st:
                    st.append(nums[i])
                elif st and nums[i]>st[-1]:
                    st.pop()
                    st.append(nums[i])
            else:
                st.append(nums[i])
        return st

class Correct:
    def largest_arr(self,nums,k):
        n=len(nums)
        if k==0: return []
        st=[]
        for i in range(len(nums)):
            # n-i>k-len(st) => no of items left > no of items we need
            while n-i>k-len(st) and st and st[-1]<nums[i]:
                st.pop()
            st.append(nums[i])
        return st


class Tester(unittest.TestCase):
    def test01(self):
        a,k=[9,1,2,5,8,3],3
        self.assertEqual(Correct().largest_arr(a,k), Solution().largest_arr(a,k))
