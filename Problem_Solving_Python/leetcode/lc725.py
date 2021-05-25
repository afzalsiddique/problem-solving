import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val) + "->" + str(self.next)
    def __eq__(self, other):
        return str(self)==str(other)
class Solution:
    def get_length(self,head):
        n=0
        while head:
            n+=1
            head=head.next
        return n
    def divide(self, length):
        if length==0: return None
        head=self.root
        last_node = self.root
        while length!=1:
            last_node=last_node.next
            length-=1
        self.root=last_node.next
        last_node.next=None
        return head
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if not root: return [None for _ in range(k)]
        self.root=root
        head=root
        n=self.get_length(head)
        len_of_parts = [n//k for _ in range(k)]
        mod = n%k
        for i in range(n%k):
            len_of_parts[i]+=1
        res=[]
        for length in len_of_parts:
            res.append(self.divide(length))
        return res

def make_linked_list(li,i=0):
    if len(li)==0: return None
    if i==len(li)-1:return ListNode(li[i])
    cur = ListNode(li[i])
    cur.next = make_linked_list(li,i+1)
    return cur
class tester(unittest.TestCase):
    def test01(self):
        root = [1,2,3]
        root = make_linked_list(root)
        k = 5
        results= [[1],[2],[3],[],[]]
        Output = []
        for res in results:
            Output.append(make_linked_list(res))
        self.assertEqual(Output, get_sol().splitListToParts(root,k))
    def test02(self):
        root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        root = make_linked_list(root)
        k = 3
        results= [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
        Output = []
        for res in results:
            Output.append(make_linked_list(res))
        self.assertEqual(Output, get_sol().splitListToParts(root,k))