import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: ListNode) -> int:
        cur=head
        li=[]
        while cur:
            li.append(cur.val)
            cur=cur.next
        n=len(li)
        res=float('-inf')
        for i in range(n//2):
            res=max(res,li[i]+li[n-i-1])
        return res

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual('981', get_sol().pairSum())
    def test_2(self):
        self.assertEqual('981', get_sol().pairSum())
    def test_3(self):
        self.assertEqual('981', get_sol().pairSum())
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
