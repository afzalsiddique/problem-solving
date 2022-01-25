import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(x): return RangeFreqQuery(x)
class RangeFreqQuery:
    # binary search
    def __init__(self, arr: List[int]):
        self.di=defaultdict(list)
        for i,x in enumerate(arr):
            self.di[x].append(i)
    def query(self, left: int, right: int, value: int) -> int:
        l_idx=bisect_left(self.di[value],left)
        r_idx=bisect_right(self.di[value],right)
        return r_idx-l_idx

class RangeFreqQuery2:
    # segment tree
    def __init__(self,arr):
        self.n=len(arr)
        self.arr=arr
        p=self.nearestPowerOf2(self.n)*2-1
        self.segment=[Counter() for _ in range(p)]
        self.construct(0,0,self.n-1)
    def construct(self, si, l, r):
        segment,arr= self.segment, self.arr
        if l==r:
            count=segment[si]
            count[arr[l]]+=1
            return count
        mid=(l+r)//2
        leftCnt=self.construct(2*si+1,l,mid)
        rightCnt=self.construct(2*si+2,mid+1,r)
        segment[si]=leftCnt+rightCnt
        return self.segment[si]
    def query(self, left, right,value):
        def helper(si,sl,sr):
            if sl>=left and sr<=right:
                cnt=segment[si][value]
                return cnt
            if sl>right or sr<left:
                return 0
            m=(sl+sr)//2
            leftCnt=helper(2*si+1,sl,m)
            rightCnt=helper(2*si+2,m+1,sr)
            return leftCnt+rightCnt

        segment=self.segment
        return helper(0,0,self.n-1)
    def nearestPowerOf2(self,i): # works for 32 bit integer
        i-=1
        i|=i>>1
        i|=i>>2
        i|=i>>4
        i|=i>>8
        i|=i>>16
        return i+1

class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='RangeFreqQuery':
                obj = get_sol(input[0])
                outputs.append(None)
            elif cmd=='query':
                outputs.append(obj.query(input[0],input[1],input[2]))
        return outputs
    def test_01(self):
        commands = ["RangeFreqQuery", "query", "query"]
        inputs=[[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
        expected = [None, 1, 2]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
