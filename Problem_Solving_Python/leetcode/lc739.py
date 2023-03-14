import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
# from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        st,n = [],len(T)
        nxt = [0] * n
        for i in range(n):
            while st and T[st[-1]]<T[i]:
                top = st.pop()
                nxt[top] = i-top
            st.append(i)
        return nxt
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([1,1,4,2,1,1,0,0], get_sol().dailyTemperatures([73,74,75,71,69,72,76,73]))
    # def test02(self):
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
