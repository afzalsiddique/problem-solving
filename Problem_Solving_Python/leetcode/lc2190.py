from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def mostFrequent(self, A: List[int], key: int) -> int:
        n=len(A)
        di=Counter()
        for i in range(1,n):
            if A[i-1]==key:
                di[A[i]]+=1
        return max(di, key=lambda x:di[x])


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(100, get_sol().mostFrequent([1,100,200,1,100], 1))
    def test02(self):
        self.assertEqual(2, get_sol().mostFrequent([2,2,2,2,3], 2))
    def test03(self):
        self.assertEqual(2, get_sol().mostFrequent([1,1000,2], 1000))
    # def test04(self):


