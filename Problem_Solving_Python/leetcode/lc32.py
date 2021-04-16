from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class Solution:
    # https://www.youtube.com/watch?v=8CYhffMML8o
    def longestValidParentheses(self, s: str) -> int:
        st = [-1]
        maxx = 0
        for i in range(len(s)):
            if s[i]=='(':st.append(i)
            else:
                st.pop()
                if not st:st.append(i)
                else:maxx=max(maxx, i-st[-1])
        return maxx

class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(2,Solution().longestValidParentheses('(()'))
    def test2(self):
        self.assertEqual(4,Solution().longestValidParentheses(')()())'))
#     def test2(self):
#     def test3(self):
