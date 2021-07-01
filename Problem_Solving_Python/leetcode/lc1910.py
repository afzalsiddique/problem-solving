import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        st=[]
        for c in s:
            st.append(c)
            if len(st)>=len(part):
                if part==''.join(st[-len(part):]):
                    for _ in range(len(part)):
                        st.pop()
        return ''.join(st)



class tester(unittest.TestCase):
    def test01(self):
        s = "daabcbaabcbc"
        part = "abc"
        Output= "dab"
        self.assertEqual(Output,get_sol().removeOccurrences(s,part))
    def test02(self):
        s = "axxxxyyyyb"
        part = "xy"
        Output= "ab"
        self.assertEqual(Output,get_sol().removeOccurrences(s,part))
