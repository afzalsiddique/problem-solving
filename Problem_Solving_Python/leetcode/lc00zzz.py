from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # It is not possible to find
    # wrong for this test case [1,1,0,0,1]
    def nextGreaterOrEqual(self,arr)->List[int]:
        n=len(arr)
        res=[-1]*n
        st=[]
        for i in range(n):
            while st and arr[st[-1]]<=arr[i]:
                idx=st.pop()
                res[idx]=i
            st.append(i)
        return res
    def maxChunksToSorted(self, arr: List[int]) -> int:
        indices=self.nextGreaterOrEqual(arr)
        # print(indices)
        i=res=0
        while i!=-1:
            i=indices[i]
            res+=1
        return res


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(1, get_sol().maxChunksToSorted(arr = [5,4,3,2,1]))
    def test02(self):
        self.assertEqual(4, get_sol().maxChunksToSorted(arr = [2,1,3,4,4]))
    def test03(self):
        self.assertEqual(6, get_sol().maxChunksToSorted(arr = [2,1,3,4,4,4,4]))
    def test04(self):
        self.assertEqual(1, get_sol().maxChunksToSorted(arr = [4,2,2,3,3]))
    def test05(self):
        self.assertEqual(2, get_sol().maxChunksToSorted(arr = [3,2,1,7,6,5]))
    def test06(self):
        self.assertEqual(2, get_sol().maxChunksToSorted(arr = [3,2,1,1,7,6,5]))
    def test07(self):
        self.assertEqual(2, get_sol().maxChunksToSorted(arr = [1,1,0,0,1]))
    def test08(self):
        self.assertEqual(1, get_sol().maxChunksToSorted(arr = [4,2,2,1,1]))
    def test09(self):
        self.assertEqual(2, get_sol().maxChunksToSorted(arr = [3,2,1,7,6,5,4]))
