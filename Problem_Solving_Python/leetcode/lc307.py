import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools;from sortedcontainers import SortedList
# from ..template.binary_tree import deserialize,serialize
def get_sol(x): return NumArray(x)
class SegmentTree:
    # https://www.youtube.com/watch?v=2bSS8rtFym4
    def __init__(self,arr):
        self.n=len(arr)
        self.arr=arr
        treeSize=self.nearestPowerOf2(len(arr))*2-1
        self.segment= [0] * treeSize
        self.construct(0, 0, self.n - 1)
    def construct(self, si, l, r):
        segment,arr= self.segment, self.arr

        if l==r:
            segment[si]=arr[l]
            return segment[si]
        mid=(l+r)//2
        segment[si]=self.construct(2*si+1,l,mid)+self.construct(2*si+2,mid+1,r) # for sum query
        return self.segment[si]
    def sumRange(self, left, right):
        def helper(si, sl, sr):
            if sl>=left and sr<=right: # total overlap
                return segment[si]
            if sl>right: return 0 # no overlap
            if sr<left: return 0 # no overlap
            # partial overlap
            mid=(sl+sr)//2
            return helper(2*si+1,sl,mid)+helper(2*si+2,mid+1,sr)

        segment=self.segment
        return helper(0,0,self.n-1)
    def update(self,i,val):
        def helper(si, sl, sr):
            if sl>i: return
            if sr<i: return
            segment[si]+=diff
            if sl!=sr:
                mid=(sl+sr)//2
                helper(2*si+1,sl,mid)
                helper(2*si+2,mid+1,sr)
            return

        segment=self.segment
        diff=val-self.arr[i]
        self.arr[i]+=diff
        return helper(0,0,self.n-1)
    def nearestPowerOf2(self,i): # works for 32 bit integer
        i-=1
        i|=i>>1
        i|=i>>2
        i|=i>>4
        i|=i>>8
        i|=i>>16
        return i+1

class NumArray:
    def __init__(self, nums: List[int]):
        self.sTree=SegmentTree(nums)
    def update(self, index: int, val: int) -> None:
        self.sTree.update(index,val)
    def sumRange(self, left: int, right: int) -> int:
        return self.sTree.sumRange(left, right)

class Tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='NumArray':
                obj = get_sol(input[0])
                outputs.append(None)
            elif cmd=='update':
                outputs.append(obj.update(input[0],input[1]))
            else:
                outputs.append(obj.sumRange(input[0],input[1]))
        return outputs
    def test_01(self):
        commands = ["NumArray", "sumRange", "update", "sumRange"]
        inputs=[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
        expected = [None, 9, None, 8]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_02(self):
        commands = ["NumArray","update","update","update","sumRange","update","sumRange","update","sumRange","sumRange","update"]
        inputs=[[[7,2,7,2,0]],[4,6],[0,2],[0,9],[4,4],[3,8],[0,4],[4,1],[0,3],[0,4],[0,4]]
        expected = [None,None,None,None,6,None,32,None,26,27,None]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)




