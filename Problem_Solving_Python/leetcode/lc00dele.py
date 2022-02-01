from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    def canSeePersonsCount(self, A):
        n=len(A)
        st = []
        res = [0] * n
        for i in range(n):
            # for ii in st: print(A[ii],end=' ')
            # print()
            while st and A[st[-1]]<A[i]:
                res[st.pop()]+=1
            if st:
                res[st[-1]]+=1
            st.append(i)
        return res

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([3,1,2,1,1,0], get_sol().canSeePersonsCount([10,12,14]))
    def test02(self):
        self.assertEqual([3,1,2,1,1,0], get_sol().canSeePersonsCount([9,6,8,5,9,9]))
    def test03(self):
        self.assertEqual([4,1,1,1,0], get_sol().canSeePersonsCount([5,1,2,3,10]))
    # def test04(self):
