from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        left,right=0,0
        while right<n:
            if nums[right]!=val:
                nums[left]=nums[right]
                left+=1
            right+=1
        return left
class Solution2:
    # def removeElement(self, nums: List[int], val: int) -> List:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i=0
        for j in range(n):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
        return i
        # return nums

class MyTestCase(unittest.TestCase):
    def test01(self):
        nums,val=[0,1,2,2,3,0,4,2],2
        length = get_sol().removeElement(nums,val)
        expected = [0,1,3,0,4]
        self.assertEqual(length,len(expected))
        for x,y in zip(expected,nums):
            self.assertEqual(x,y)
    def test02(self):
        nums,val=[3,2,2,3],3
        length = get_sol().removeElement(nums,val)
        expected = [2,2]
        self.assertEqual(length,len(expected))
        for x,y in zip(expected,nums):
            self.assertEqual(x,y)
    def test03(self):
        nums,val=[0,1,2,2,3,0,4,2],2
        length = get_sol().removeElement(nums,val)
        expected = [0,1,3,0,4]
        self.assertEqual(length,len(expected))
        for x,y in zip(expected,nums):
            self.assertEqual(x,y)
    def test04(self):
        nums,val=[3,2,2,3],3
        length = get_sol().removeElement(nums,val)
        expected = [2,2]
        self.assertEqual(length,len(expected))
        for x,y in zip(expected,nums):
            self.assertEqual(x,y)
