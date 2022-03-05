from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def simplifyPath(self, s: str) -> str:
        n=len(s)
        i=0
        res=[]
        while i<n:
            j=i
            while j<n and s[j]!='/':
                j+=1
            tmp=s[i:j]
            i=j+1
            if tmp=='': continue
            if tmp=='.': continue
            if tmp=='..':
                if res: res.pop()
            else:
                res.append(tmp)
        return '/'+'/'.join(res)
class Solution2:
    def mySplit(self,s):
        n=len(s)
        i=0
        li=[]
        while i<n:
            j=i
            while j<n and s[j]!='/':
                j+=1
            li.append(s[i:j])
            i=j+1
        return li
    def simplifyPath(self, s: str) -> str:
        li = self.mySplit(s)
        res=[]
        for x in li:
            if x=='': continue
            if x=='.': continue
            if x=='..':
                if res:
                    res.pop()
            else:
                res.append(x)
        return '/'+'/'.join(res)


class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual( "/home",get_sol().simplifyPath("/home/"))
    def test2(self):
        self.assertEqual( "/" ,get_sol().simplifyPath("/../"))
    def test3(self):
        self.assertEqual( "/home/foo" ,get_sol().simplifyPath("/home//foo/"))
    def test4(self):
        self.assertEqual( "/c" ,get_sol().simplifyPath("/a/./b/../../c/"))
    def test5(self):
        self.assertEqual( "/a/b/c" ,get_sol().simplifyPath("/a//b////c/d//././/.."))
