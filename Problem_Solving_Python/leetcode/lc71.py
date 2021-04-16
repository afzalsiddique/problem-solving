import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class Solution:
    def simplifyPath(self, path: str) -> str:
        def my_split(path):
            res = []
            n=len(path)
            left, right= 0, 0
            while right<n:
                if path[right]=='/':
                    res.append(path[left:right])
                    left=right+1
                right+=1
            res.append(path[left:right]) # append the last one
            return res
        # path2=path.split('/') # this one also works
        # print(path2)
        path = my_split(path)
        # print(path)
        st,res=[],[]
        for x in path:
            if len(x)==0: continue
            if x=='.': continue
            if x=='..' and not st: continue
            if x=='..' and st:
                st.pop()
                continue
            st.append(x)
        if not st: return '/'
        return '/' + '/'.join(st)

class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual( "/home",Solution().simplifyPath("/home/"))
    def test2(self):
        self.assertEqual( "/" ,Solution().simplifyPath("/../"))
    def test3(self):
        self.assertEqual( "/home/foo" ,Solution().simplifyPath("/home//foo/"))
    def test4(self):
        self.assertEqual( "/c" ,Solution().simplifyPath("/a/./b/../../c/"))
    def test5(self):
        self.assertEqual( "/a/b/c" ,Solution().simplifyPath("/a//b////c/d//././/.."))
