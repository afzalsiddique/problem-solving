from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    def maxChunksToSorted(self, arr) -> int:
        n=len(arr)
        left_max=list(accumulate(arr,lambda a,b:max(a,b)))
        right_min=list(accumulate(arr[::-1],lambda a,b:min(a,b)))[::-1]
        res=1
        for i in range(n-1):
            if left_max[i]<=right_min[i+1]:
                res+=1
        return res

class Solution3:
    # Tried finding next greater or equal.
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
        i=res=0
        while i!=-1:
            i=indices[i]
            res+=1
        return res
class Solution2:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)

        max_left=[-1]*n
        max_left[0]=arr[0]
        for i in range(1,n):
            max_left[i]=max(max_left[i-1],arr[i])

        min_right=[-1]*n
        min_right[-1]=arr[-1]
        for i in range(n-2,-1,-1):
            min_right[i]=min(min_right[i+1],arr[i])

        res=1
        for i in range(n-1):
            if max_left[i]<=min_right[i+1]:
                res+=1 # i is the last index of the current chunk
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
        self.assertEqual(2, get_sol().maxChunksToSorted(arr = [0,3,0,3,2]))
    def test09(self):
        self.assertEqual(1, get_sol().maxChunksToSorted(arr = [4,2,2,1,1]))
    def test10(self):
        self.assertEqual(2, get_sol().maxChunksToSorted(arr = [3,2,1,7,6,5,4]))
