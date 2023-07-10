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
    def push(self, val, idx): heappush(self, [val*self.mul, idx*self.mul])
    def heappop(self):
        tmp=heappop(self)
        return [tmp[0]*self.mul, tmp[1]*self.mul]
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def ways(a,b):
            li = [a+b,a-b,b-a,a*b]
            if b!=0: li.append(a/b)
            if a!=0: li.append(b/a)
            return li
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def getMedian():
            if k&1:
                return float(right.topVal())
            return (left.topVal()+right.topVal()) / 2
        def move(frm:Heap,to:Heap):
            to.push(*frm.heappop())
        def clearTop(i):
            while left and left.topIdx()<=i:
                left.heappop()
            while right and right.topIdx()<=i:
                right.heappop()

        if k==1: return list(map(float,nums))
        res=[]
        left,right=Heap(True),Heap() # minHeap contains more elements if odd
        for i in range(k):
            right.push(nums[i],i)
        for _ in range(k//2):
            move(right,left)
        res.append(getMedian())

        for i in range(k,len(nums)):
            if nums[i-k]<=left.topVal(): # expiring on the left
                left.push(nums[i],i)
            else:
                right.push(nums[i],i)
            move(left,right)
            move(right,left)
            clearTop(i-k)
            res.append(getMedian())
        return res



class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual("7772", get_sol().largestNumber([4,3,2,5,6,7,2,5,5], 9))
    def test2(self):
        self.assertEqual("85", get_sol().largestNumber( [7,6,5,5,5,6,8,7,8], 12))
    def test3(self):
        self.assertEqual("0", get_sol().largestNumber([2,4,6,2,4,6,4,4,4], 5))
    def test4(self):
        self.assertEqual("0", get_sol().largestNumber([210,77,91,105,1208,511,3392,3029,1029], 4031))
    def test5(self):
        self.assertEqual("87432222222222222222222222222222222222222222222", get_sol().largestNumber([210,77,91,105,1908,3953,530,410,1237], 4447))
    def test6(self):
        self.assertEqual("5555443222", get_sol().largestNumber([1000,30,105,70,42,1000,1000,1000,1000], 503))
    # def test7(self):
    # def test8(self):
