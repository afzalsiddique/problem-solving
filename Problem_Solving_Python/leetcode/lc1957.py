import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    def makeFancyString(self, s: str) -> str:
        n=len(s)
        l,r=0,0
        res=[]
        while r<n:
            while r<n and s[r]==s[l]:
                if r-l<2:
                    res.append(s[r])
                r+=1
            l=r
        return ''.join(res)
