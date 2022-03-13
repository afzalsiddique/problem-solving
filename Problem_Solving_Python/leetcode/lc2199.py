from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def findKDistantIndices(self, A: List[int], key: int, k: int) -> List[int]:
        n=len(A)
        res=[]
        for i in range(n):
            for j in range(max(0,i-k),min(n,i+k+1)):
                if A[j]==key:
                    res.append(i)
                    break
        return res

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([1,2,3,4,5,6], get_sol().findKDistantIndices([3,4,9,1,3,9,5], 9, 1))
    def test02(self):
        self.assertEqual([0,1,2,3,4], get_sol().findKDistantIndices([2,2,2,2,2], 2, 2))
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
