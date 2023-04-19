from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional,Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class MaxHeap(list):
    def __init__(self):
        super().__init__()
    def push(self,x):
        heappush(self,x)
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def dp(i,j,k):
            if k==0:
                return []
            res=[]
            select1,not_select1,select2,not_select2=[],[],[],[]
            if i<m and j<n:
                not_select1=dp(i+1,j,k)
                select1=[nums1[i]]+dp(i+1,j,k-1)
                not_select2=dp(i,j+1,k)
                select2=[nums2[j]]+dp(i,j+1,k-1)
            elif i==m:
                not_select2=dp(i,j+1,k)
                select2=[nums2[j]]+dp(i,j+1,k-1)
            else:
                not_select1=dp(i+1,j,k)
                select1=[nums1[i]]+dp(i+1,j,k-1)
            res=max(res,not_select1,select1,not_select2,select2)
            return res




        m,n=len(nums1),len(nums2)
        return recur(0,0)+len(key)

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(4, get_sol().lengthOfLIS([10,9,2,5,3,7,101,18]))
    def test_2(self):
        self.assertEqual(4, get_sol().lengthOfLIS([0,1,0,3,2,3]))
    def test_3(self):
        self.assertEqual(1, get_sol().lengthOfLIS([7,7,7,7,7,7,7]))
    def test_4(self):
        self.assertEqual(6, get_sol().lengthOfLIS([1,3,6,7,9,4,10,5,6]))
    def test_5(self):
        self.assertEqual(6, get_sol().lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]))
    def test_6(self):
        self.assertEqual(3, get_sol().lengthOfLIS([1,2,-10,-8,-7]))
