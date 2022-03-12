from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
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

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(2,get_sol().longestValidParentheses('(()'))
    def test02(self):
        self.assertEqual(4,get_sol().longestValidParentheses(')()())'))
    def test03(self):
        self.assertEqual(0,get_sol().longestValidParentheses(''))
    def test04(self):
        self.assertEqual(2,get_sol().longestValidParentheses('()(()'))
