import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        def calc(di,x):
            li=di[x]
            pre=[0]+list(itertools.accumulate(li))
            newLi=[]
            for i in li:
                newLi.append(len(li)-i)
            newLi.reverse()
            suf=list(reversed(list(itertools.accumulate(newLi))))+[0]
            cnt={}
            for i,idx in enumerate(li):
                cnt[idx]=i*idx
                cnt[idx]-=pre[i]
                newI=len(li)-1-i
                newIdx=n-1-idx
                cnt[idx]+=newI*newIdx
                cnt[idx]-=suf[newI]
            return cnt

        n=len(arr)
        di1=defaultdict(list)
        # di2=defaultdict(list)
        for i,x in enumerate(arr):
            di1[x].append(i)
            # di2[x].append(n-1-i)

        vis=set()
        res=[0]*n
        for x in arr:
            if x in vis: continue
            vis.add(x)
            tmp=calc(di1,x)
            for i,v in tmp:
                res[i]=v
        return res

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([4,2,7,2,4,4,5], get_sol().getDistances([2,1,3,1,2,3,3]))
    def test2(self):
        self.assertEqual([5,0,3,4], get_sol().getDistances([10,5,10,10]))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):
