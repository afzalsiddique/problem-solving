from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list,ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class MaxHeap(list):
    def __init__(self): super().__init__()
    def heappop(self): return heappop(self)[0]*(-1)
    def push(self,a,b): heappush(self,[-a,-b])

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mx_heap=MaxHeap()
        mx_heap.push(1,2)
        mx_heap.push(3,2)
        mx_heap.push(2,2)
        print(mx_heap)


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([0,3,1,2,4], get_sol().addTwoNumbers([0,1,1,2,4], [0,1,0,0,1]))
    def test2(self):
        self.assertEqual([0,2,1], get_sol().timeTaken([0,0,0], [1,0,1]))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):
