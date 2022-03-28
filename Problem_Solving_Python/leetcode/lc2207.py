from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def halveArray(self, A: List[int]) -> int:
        cur=sum(A)
        target=sum(A)/2
        pq=[-x for x in A]
        heapify(pq)
        res=0
        while cur>target:
            val=heappop(pq)
            val*=(-1) # max_heap
            val=val/2
            cur-=val
            heappush(pq,val*(-1))
            res+=1
        return res


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(3,get_sol().halveArray([5,19,8,1]))
    def test02(self):
        self.assertEqual(3,get_sol().halveArray([3,8,20]))
    def test03(self):
        self.assertEqual(1,get_sol().halveArray([8]))
