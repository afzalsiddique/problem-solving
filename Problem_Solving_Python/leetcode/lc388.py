import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution3()
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        def get_tab_count(s):
            n=len(s)
            i=0
            res=0
            while i<n:
                if s[i]=="\t":
                    i+=1
                    res+=1
                else:
                    break
            return res

        di = defaultdict()
        di[-1]=0
        maxx = 0
        li = input.split('\n')
        for s in li:
            tab_cnt = get_tab_count(s)
            # path_length = prev_path_length + cur file/dir length - tab_cnt + 1  # '+1' for '/'
            di[tab_cnt]=di[tab_cnt-1]+len(s)-tab_cnt +1 # '+1' for '/'
            if '.' in s:
                maxx=max(maxx,di[tab_cnt])

        maxx-=1 # the very first '/'
        return max(0,maxx)
class Solution2:
    def lengthLongestPath(self, input: str) -> int:
        def get_tab_count(s):
            n=len(s)
            i=0
            res=0
            while i<n:
                if s[i]=="\t":
                    i+=1
                    res+=1
                else:
                    break
            return res, s[res:]

        di = defaultdict()
        di[-1]=""
        maxx = 0
        li = input.split('\n')
        for s in li:
            cnt,s = get_tab_count(s)
            di[cnt]=di[cnt-1]+'/'+s
            if '.' in s:
                maxx=max(maxx,len(di[cnt]))

        maxx-=1 # the very first '/'
        return max(0,maxx)

class Solution3:
    def lengthLongestPath(self, input: str) -> int:
        def get_tab_count(s):
            n=len(s)
            i=0
            res=0
            while i<n:
                if s[i]=="\t":
                    i+=1
                    res+=1
                else:
                    break
            return res, s[res:]

        di = defaultdict(list)
        di[-1].append("")
        li = input.split('\n')
        for s in li:
            cnt,s = get_tab_count(s)
            di[cnt].append(di[cnt-1][-1]+'/'+s)

        maxx = 0
        for key in di:
            for file_path in di[key]:
                if '.' in file_path:
                    maxx=max(maxx,len(file_path))
        maxx-=1 # the very first '/'
        return max(0,maxx)
class MyTestCase(unittest.TestCase):
    def test1(self):
        input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
        Output= 20
        self.assertEqual(Output, get_sol().lengthLongestPath(input))
    def test2(self):
        input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
        Output= 32
        self.assertEqual(Output, get_sol().lengthLongestPath(input))
    def test3(self):
        input = "a"
        Output= 0
        self.assertEqual(Output, get_sol().lengthLongestPath(input))
    def test4(self):
        input = "file1.txt\nfile2.txt\nlongfile.txt"
        Output= 12
        self.assertEqual(Output, get_sol().lengthLongestPath(input))
    # def test5(self):
    # def test6(self):
