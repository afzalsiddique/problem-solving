from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=2ayws5Y-WM4
    # time O(26n) space O(26)
    def removeDuplicateLetters(self, s: str) -> str:
        lastOccurence={c:i for i,c in enumerate(s)}
        st=[] # increasing stack of letters. maximum possible length is 26
        for i,c in enumerate(s):
            if c not in st:
                while st and i<lastOccurence[st[-1]] and c<st[-1]:
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
        self.assertEqual('abc',get_sol().removeDuplicateLetters('bcabc'))
    def test2(self):
        self.assertEqual("acdb",get_sol().removeDuplicateLetters("cbacdcbc"))
    def test3(self):
        self.assertEqual("abc",get_sol().removeDuplicateLetters("abacb"))
