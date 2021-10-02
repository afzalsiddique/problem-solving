import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/discuss/1032339/PythonDraw-a-simple-graph-to-explain
    def minCharacters(self, a: str, b: str) -> int:
        m,n=len(a),len(b)
        freq1 = [0]*26
        freq2 = [0]*26
        for x in a: freq1[ord(x)-97]+=1
        for x in b: freq2[ord(x)-97]+=1
        most_common = float('-inf')
        for i in range(26):
            most_common = max(most_common, freq1[i]+freq2[i])
        option3 = m+n-most_common

        pre1 = list(itertools.accumulate(freq1))
        pre2 = list(itertools.accumulate(freq2))

        option1,option2=float('inf'),float('inf')
        for i in range(25): # avoid 'z'. you cant move letters in b to be on the right of z
            option1 = min(option1,pre1[i]+n-pre2[i])
            option2 = min(option2,pre2[i]+m-pre1[i])
        return min(option1,option2,option3)


class MyTestCase(unittest.TestCase):
    def test1(self):
        a,b = "aba", "caa"
        Output= 2
        self.assertEqual(Output, get_sol().minCharacters(a,b))
    def test2(self):
        a,b = "dabadd", "cda"
        Output= 3
        self.assertEqual(Output, get_sol().minCharacters(a,b))
    def test3(self):
        a,b = "da", "cced"
        Output= 1
        self.assertEqual(Output, get_sol().minCharacters(a,b))
    def test4(self):
        a,b = "e", "e"
        Output= 0
        self.assertEqual(Output, get_sol().minCharacters(a,b))