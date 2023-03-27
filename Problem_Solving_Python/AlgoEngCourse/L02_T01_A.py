from itertools import accumulate; from math import floor,ceil,sqrt,log,log2; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt

class SegmentTree:
    def __init__(self,arr):
        self.n=len(arr)
        self.arr=arr
        treeSize=self.nearestPowerOf2(len(arr))*2-1
        self.segment= [0] * treeSize
        self.construct()
    def construct(self): # O(n)
        def helper(si,l,r):
            if l==r:
                segment[si]=arr[l]
                return segment[si]
            mid=(l+r)//2
            ans1=helper(2*si+1,l,mid)
            ans2=helper(2*si+2,mid+1,r)
            segment[si]=min(ans1,ans2)
            return self.segment[si]

        segment,arr= self.segment, self.arr
        helper(0,0,self.n-1)
    def minRange(self, left, right): # O(logn)
        def helper(si, sl, sr):
            if sl>=left and sr<=right: # total overlap
                return segment[si]
            if sl>right: return float('inf') # no overlap
            if sr<left: return float('inf') # no overlap
            # partial overlap
            mid=(sl+sr)//2
            ans1=helper(2*si+1,sl,mid)
            ans2=helper(2*si+2,mid+1,sr)
            return min(ans1,ans2)

        segment=self.segment
        return helper(0,0,self.n-1)
    def nearestPowerOf2(self,i): # nearest power of 2 which is greater or equal to i. Works for 32 bit integer
        i-=1
        i|=i>>1
        i|=i>>2
        i|=i>>4
        i|=i>>8
        i|=i>>16
        return i+1

class MinSparseTable:
    def __init__(self,arr:List[int]):
        self.arr = arr
        self.buildTable(arr)
    def buildTable(self,arr:List[int]): # O(n*logn)
        n=len(arr)
        noOfRows = int(log(n) / log(2))
        self.dp = [[0]*n for _ in range(noOfRows+1)]

        for j in range(n):
            self.dp[0][j] = arr[j]

        for i in range(1,noOfRows+1):
            j=0
            while j + (1 << i) <= n:
            # while j + (1 << (i-1)) < n:
                leftInterval = self.dp[i-1][j]
                rightInterval = self.dp[i-1][j + (1 << (i - 1))]
                self.dp[i][j] = min(leftInterval,rightInterval)
                j+=1

    def minQuery(self,l,r): # O(1)
        length = r-l+1
        p = floor(log2(length))
        k = 1<<p
        return min(self.dp[p][l],self.dp[p][r-k+1])

def runSegTree(s:str):
    inputs = convert_input(s)
    arr = inputs[1]
    sTree = SegmentTree(arr)
    q = inputs[2][0]
    res = []
    for i in range(3,q+3):
        l,r = inputs[i]
        res.append(sTree.minRange(l,r))
    return res

def runSparseTable(s:str):
    inputs = convert_input(s)
    arr = inputs[1]
    sTable = MinSparseTable(arr)
    q = inputs[2][0]
    res = []
    for i in range(3,q+3):
        l,r = inputs[i]
        res.append(sTable.minQuery(l,r))
    return res

def convert_input(s:str)->List[List[int]]:
    s = s.split('\n')
    s = list(map(lambda x:x.split(" "), s))
    s = list(map(lambda li:[int(x) for x in li],s))
    return s

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([4,1,1,1],runSegTree("3"
                                    "\n1 4 1"
                                    "\n4"
                                    "\n1 1"
                                    "\n2 2"
                                    "\n0 2"
                                    "\n0 1"))
    def test2(self):
        self.assertEqual([4,1,1,1],runSparseTable("3"
                                              "\n1 4 1"
                                              "\n4"
                                              "\n1 1"
                                              "\n2 2"
                                              "\n0 2"
                                              "\n0 1"))
