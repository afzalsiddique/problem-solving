import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def minimumBuckets(self, street: str) -> int:
        n=len(street)
        if n==1:
            if street[0]=='H': return -1
            return 0

        res=0
        collecting = [True]*n
        for i in range(n):
            if street[i]=='H':
                collecting[i]=False
        for i in range(1,n-1):
            if street[i]=='.' and street[i-1]=='H' and street[i+1]=='H' and not collecting[i-1] and not collecting[i+1]:
                res+=1
                collecting[i-1]=True
                collecting[i+1]=True
        for i in range(n):
            if collecting[i]: continue
            # if i==0 and street[i+1]=='H': return -1
            # if i==n-1 and street[i-1]=='H': return -1
            # if street[i-1]=='H' and street[i+1]=='H': return -1
            if street[i-1]=='.':
                collecting[i-1]=True
                res+=1
            else:
                collecting[i+1]=True
                res+=1
        return res


class MyTestCase(unittest.TestCase):
    def test1(self):
        street = "H..H"
        Output= 2
        self.assertEqual(Output, get_sol().minimumBuckets(street))
    def test2(self):
        street = ".H.H."
        Output= 1
        self.assertEqual(Output, get_sol().minimumBuckets(street))
    def test3(self):
        street = ".HHH."
        Output= -1
        self.assertEqual(Output, get_sol().minimumBuckets(street))
    def test4(self):
        street = "H"
        Output= -1
        self.assertEqual(Output, get_sol().minimumBuckets(street))
    def test5(self):
        street = "."
        Output= 0
        self.assertEqual(Output, get_sol().minimumBuckets(street))
    def test6(self):
        street = ".HH.H.H.H.."
        Output= 3
        self.assertEqual(Output, get_sol().minimumBuckets(street))
    def test7(self):
        street = "HH........"
        Output= -1
        self.assertEqual(Output, get_sol().minimumBuckets(street))
    # def test8(self):
