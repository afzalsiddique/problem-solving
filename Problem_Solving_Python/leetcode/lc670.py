from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=pDyh9VOMWgI&t=548s
    def maximumSwap(self, num: int) -> int:
        li = list(map(int, str(num)))
        index = {x:i for i,x in enumerate(li)}
        for i,x in enumerate(li):
            for y in reversed(range(10)):
                if y in index and index[y]>i and y>x:
                    li[i],li[index[y]] = li[index[y]],li[i]
                    return int(''.join(map(str,li)))
        return num
class Solution2:
    def maximumSwap(self, num: int) -> int:
        li = list(str(num))
        temp = li[:]
        i=0
        while temp:
            maxx = max(temp)
            if maxx!=li[i]:
                break
            temp.remove(maxx)
            i+=1
        if not temp: return num
        idx=li[::-1].index(maxx) # get the last max if multiple. that's why reversed
        idx = len(li)-1-idx
        li[i],li[idx]=li[idx],li[i]
        li = ''.join(li)
        li = int(li)
        return li
class Solution3:
    def maximumSwap(self, num: int) -> int:
        li=[int(c) for c in str(num)]
        n=len(li)

        leftMin=[[float('inf'),-1]]*n
        minn=float('inf')
        for i in range(n):
            if li[i]<minn:
                minn=li[i]
                leftMin[i]=[minn,i]
            else:
                leftMin[i]=leftMin[i-1]

        rightMax=[[float('inf'),-1]]*n
        maxx=float('-inf')
        for i in range(n-1,-1,-1):
            if li[i]>maxx:
                maxx=li[i]
                rightMax[i]=[maxx,i]
            else:
                rightMax[i]=rightMax[i+1]
        i=0
        while i<len(li) and leftMin[i][0]>=rightMax[i][0]:
            i+=1
        if i==len(li): return num
        leftIdx=leftMin[i][1]
        rightIdx=rightMax[i][1]
        li[leftIdx],li[rightIdx]=li[rightIdx],li[leftIdx]
        return int(''.join(map(str,li)))
class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(0, get_sol().maximumSwap(0))
    def test02(self):
        self.assertEqual(1, get_sol().maximumSwap(1))
    def test03(self):
        self.assertEqual(98, get_sol().maximumSwap(98))
    def test04(self):
        self.assertEqual(98, get_sol().maximumSwap(89))
    def test05(self):
        self.assertEqual(88, get_sol().maximumSwap(88))
    def test06(self):
        self.assertEqual(7236, get_sol().maximumSwap(2736))
    def test07(self):
        self.assertEqual(9973, get_sol().maximumSwap(9973))
    def test08(self):
        self.assertEqual(999, get_sol().maximumSwap(999))
    def test09(self):
        self.assertEqual(98863, get_sol().maximumSwap(98368))
    def test10(self):
        self.assertEqual(511, get_sol().maximumSwap(115))
    def test11(self):
        self.assertEqual(90909011, get_sol().maximumSwap(10909091))
    def test12(self):
        self.assertEqual(99910, get_sol().maximumSwap(99901))
    def test13(self):
        self.assertEqual(63454, get_sol().maximumSwap(43456))
