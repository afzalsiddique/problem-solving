import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        di={c:i for i,c in enumerate(s)}
        st=[]
        for i,c in enumerate(s):
            if c not in st:
                while st and i<di[st[-1]] and c<st[-1]:
                    st.pop()
                st.append(c)
        return ''.join(st)

class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual('abc',Solution().smallestSubsequence('bcabc'))
    def test2(self):
        self.assertEqual("acdb",Solution().smallestSubsequence("cbacdcbc"))
    def test3(self):
        self.assertEqual("abc",Solution().smallestSubsequence("abacb"))
