import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self): return str(self.val) + "->" + str(self.next)
    def __eq__(self, other): return str(self)==str(other)

def make_linked_list(li,i=0):
    if not li: return None
    if i==len(li)-1:return ListNode(li[i])
    cur = ListNode(li[i])
    cur.next = make_linked_list(li,i+1)
    return cur
class Solution:
    def numComponents(self, head: ListNode, nums: List[int]) -> int:
        sett= set(nums)
        res = 0
        while head:
            flag=False
            while head and head.val in sett:
                flag=True
                head=head.next
            if flag:
                res+=1
            if head:
                head=head.next
        return res
class MyTestCase(unittest.TestCase):
    def test1(self):
        head,nums = make_linked_list([0,1,2,3]),  [0,1,3]
        Output= 2
        self.assertEqual(Output, get_sol().numComponents(head,nums))
    def test2(self):
        head,nums = make_linked_list([0,1,2,3,4]),  [0,3,1,4]
        Output= 2
        self.assertEqual(Output, get_sol().numComponents(head,nums))
    def test3(self):
        head,nums = make_linked_list([3,4,0,2,1]),  [4]
        Output= 1
        self.assertEqual(Output, get_sol().numComponents(head,nums))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
