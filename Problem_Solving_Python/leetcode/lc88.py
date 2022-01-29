from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des
def get_sol(): return Solution()
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j,k=m-1,n-1,m+n-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1

        while i>=0:
            nums1[k]=nums1[i]
            i-=1
            k-=1
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1


# class MyTestCase(unittest.TestCase):
    # def test01(self):
    # def test02(self):
    # def test03(self):
    # def test04(self):
    # def test05(self):
