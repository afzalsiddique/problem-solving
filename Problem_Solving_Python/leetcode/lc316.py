import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

# https://www.youtube.com/watch?v=2ayws5Y-WM4
# time O(26n) space O(26)
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        di={c:i for i,c in enumerate(s)}
        st=[]
        for i,c in enumerate(s):
            if c not in st:
                while st and i<di[st[-1]] and c<st[-1]:
                    st.pop()
                st.append(c)
        return ''.join(st)

# Wrong
class Solution2:
    def removeDuplicateLetters(self, s: str) -> str:
        di={c:i for i,c in enumerate(s)}
        st=[]
        for i,c in enumerate(s):
            while st and c<st[-1] and di[st[-1]]>i:
                st.pop()
            if c not in st:
                st.append(c)
        return ''.join(st)
class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual('abc',Solution().removeDuplicateLetters('bcabc'))
    def test2(self):
        self.assertEqual("acdb",Solution().removeDuplicateLetters("cbacdcbc"))
    def test3(self):
        self.assertEqual("abc",Solution().removeDuplicateLetters("abacb"))
