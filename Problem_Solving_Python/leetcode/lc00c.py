import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def is_subsequence(s,p,k):
            sett=set()
            for i in range(k):
                sett.add(removable[i])

            i,j=0,0
            while i<len(s) and j<len(p):
                if i in sett:
                    i+=1
                    continue
                if s[i]==p[j]:
                    i+=1
                    j+=1
                else:
                    i+=1
            if j==len(p): return True
            return False

        lo=0
        hi=len(removable)
        while lo<=hi:
            mid = (lo+hi)//2
            if is_subsequence(s,p,mid):
                lo=mid+1
            else:
                hi=mid-1
        return lo-1




class tester(unittest.TestCase):
    def test01(self):
        s = "abcacb"
        p = "ab"
        removable = [3,1,0]
        Output= 2
        self.assertEqual(Output,get_sol().maximumRemovals(s,p,removable))
    def test02(self):
        s = "abcbddddd"
        p = "abcd"
        removable = [3,2,1,4,5,6]
        Output= 1
        self.assertEqual(Output,get_sol().maximumRemovals(s,p,removable))
    def test03(self):
        s = "abcab"
        p = "abc"
        removable = [0,1,2,3,4]
        Output= 0
        self.assertEqual(Output,get_sol().maximumRemovals(s,p,removable))
