from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Heap(list):
    def __init__(self,isMaxHeap=False):
        super().__init__()
        self.mul=-1 if isMaxHeap else 1
    def topVal(self)->int: return self[0][0]*self.mul
    def topIdx(self)->int: return self[0][1]*self.mul
    def setTopVal(self,val): self[0][0]=val*self.mul
    def setTopIdx(self,val): self[0][1]=val*self.mul
    def push(self, val, idx): heappush(self, [val*self.mul, idx*self.mul])
    def heappop(self):
        tmp=heappop(self)
        return [tmp[0]*self.mul, tmp[1]*self.mul]
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def getMedian():
            if k&1:
                return mnHeap.topVal()
            return (mxHeap.topVal()+mnHeap.topVal()) // 2
        def move(frm:Heap,to:Heap):
            to.push(*frm.heappop())
        def clearTop(i):
            while mxHeap and mxHeap.topIdx()<=i:
                mxHeap.heappop()
            while mnHeap and mnHeap.topIdx()<=i:
                mnHeap.heappop()

        res=[]
        mxHeap,mnHeap=Heap(True),Heap() # minHeap contains more elements if odd
        for i in range(k):
            mnHeap.push(nums[i],i)
        for _ in range(k//2):
            move(mnHeap,mxHeap)
        res.append(getMedian())

        for i in range(k,len(nums)):
            if nums[i-k]>=mnHeap.topVal(): # expiring on the mxHeap
                clearTop(i-k)
                mnHeap.push(nums[i],i)
            else:
                clearTop(i-k)
                mxHeap.push(nums[i],i)
            move(mxHeap,mnHeap)
            move(mnHeap,mxHeap)
            res.append(getMedian())
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
        nums, k = [2147483647,1,2,3,4,5,6,7,2147483647], 2
        Output= [1073741824.0, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 1073741827.0]
        self.assertEqual(Output, get_sol().medianSlidingWindow(nums,k))
    def test5(self):
        nums, k = [1,3,-1,-3],3
        Output= [1.00000,-1.00000]
        self.assertEqual(Output, get_sol().medianSlidingWindow(nums,k))
    def test6(self):
        nums, k = [1,3,-1,-3,5,3],3
        Output= [1.00000,-1.00000,-1.00000,3.00000]
        self.assertEqual(Output, get_sol().medianSlidingWindow(nums,k))
    # def test7(self):
    # def test8(self):
