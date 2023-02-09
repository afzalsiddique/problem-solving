from itertools import accumulate; from math import floor,ceil,sqrt,log,log2; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
def get_sol(): return Solution()
class SegmentTree:
    def __init__(self,arr):
        self.n=len(arr)
        self.arr=arr
        treeSize=self.nearestPowerOf2(len(arr))*2-1
        self.segment= [0] * treeSize
        self.construct()
    def construct(self):
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
    def minQuery(self, left, right):
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
    def buildTable(self,arr:List[int]):
        n=len(arr)
        noOfRows = int(log(n) / log(2))
        self.dp = [[0]*n for _ in range(noOfRows+1)]

        for j in range(n):
            self.dp[0][j] = arr[j]

        for i in range(1,noOfRows+1):
            j=0
            while j + (1 << i) <= n:
                leftInterval = self.dp[i-1][j]
                rightInterval = self.dp[i-1][j + (1 << (i - 1))]
                self.dp[i][j] = min(leftInterval,rightInterval)
                j+=1

    def minQuery(self,l,r):
        length = r-l+1
        p = floor(log2(length))
        k = 1<<p
        return min(self.dp[p][l],self.dp[p][r-k+1])

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def get_imbal(c): return 1 if c=='(' else -1
        n=len(s)
        imbal_sum = [0]*(n+1)
        imbal_idx = defaultdict(list)
        imbal_idx[0].append(-1)

        for i in range(n):
            imbal_sum[i+1] = get_imbal(s[i]) + imbal_sum[i]
            sm = imbal_sum[i+1]
            imbal_idx[sm].append(i)

        sgmin = SegmentTree(imbal_sum)
        maxlen = 0

        for val, idx in imbal_idx.items():
            curlen = 0
            lastidx=idx[0]

            for j in range(1,len(idx)):
                curidx = idx[j]
                if val == sgmin.minQuery(lastidx + 1, curidx + 1):
                    curlen += curidx - lastidx
                else:
                    curlen = 0
                lastidx = curidx
                maxlen = max(maxlen, curlen)

        return maxlen


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(2,get_sol().longestValidParentheses('(()'))
    def test02(self):
        self.assertEqual(4,get_sol().longestValidParentheses(')()())'))
    def test03(self):
        self.assertEqual(0,get_sol().longestValidParentheses(''))
    def test04(self):
        self.assertEqual(2,get_sol().longestValidParentheses('()(()'))
    def test05(self):
        self.assertEqual(0,get_sol().longestValidParentheses(')('))
