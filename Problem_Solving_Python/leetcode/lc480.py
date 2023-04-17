from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class MaxHeap(list):
    def __init__(self):
        super().__init__()
    def topVal(self): return -self[0][0]
    def topIdx(self): return self[0][1]
    def push(self, val, idx): heappush(self, [-val, idx])
    def heappop(self):
        val,idx=heappop(self)
        return [-val,idx]
class MinHeap(list):
    def __init__(self):
        super().__init__()
    def topVal(self): return self[0][0]
    def topIdx(self): return self[0][1]
    def push(self, val, idx): heappush(self, [val, idx])
    def heappop(self):
        val,idx=heappop(self)
        return [val,idx]
class Solution:
    # https://leetcode.com/problems/sliding-window-median/solutions/262689/python-small-large-heaps/
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def move(frm,to):
            to.push(*frm.heappop())
        def isGoingToRight(x):
            return x>right.topVal()
        def getMed():
            if k%2: return float(right.topVal())
            else: return (right.topVal()+left.topVal())/2


        if k==1: return nums
        left,right=MaxHeap(),MinHeap() # right contains one more numbers if k is odd. left is maxheap and right is minheap
        res=[]
        for i in range(k):
            right.push(nums[i],i)
        for i in range(k//2):
            move(right,left)

        res.append(getMed())

        for i in range(k,len(nums)):
            x = nums[i]
            if isGoingToRight(x):
                right.push(x,i)
                if nums[i-k]<=left.topVal():# nums[i-k] is expiring. expiring num is in the left side. So add another num from the right to the left
                    move(right,left)
            else:
                left.push(x,i)
                if nums[i-k]>=right.topVal(): # expiring num is in the right side. So add another num from the left to the right
                    move(left,right)
            while left and left.topIdx()<=i-k:
                left.heappop()
            while right and right.topIdx()<=i-k:
                right.heappop()
            res.append(getMed())
        return res



class MyTestCase(unittest.TestCase):
    def test1(self):
        nums, k = [1,3,-1,-3,5,3,6,7],3
        Output= [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
        self.assertEqual(Output, get_sol().medianSlidingWindow(nums,k))
    def test2(self):
        nums, k = [1,2,3,4,2,3,1,4,2], 3
        Output= [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
        self.assertEqual(Output, get_sol().medianSlidingWindow(nums,k))
    def test3(self):
        nums, k = [1,2], 1
        Output= [1.00000,2.00000]
        self.assertEqual(Output, get_sol().medianSlidingWindow(nums,k))
    def test4(self):
        self.assertEqual([1073741824.0, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 1073741827.0], get_sol().medianSlidingWindow([2147483647,1,2,3,4,5,6,7,2147483647], 2))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
