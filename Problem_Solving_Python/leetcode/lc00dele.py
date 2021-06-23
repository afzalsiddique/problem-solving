import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self): return str(self.val) + "->" + str(self.next)
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n=0
        dummy = ListNode(0,head)
        node = dummy
        while node:
            node=node.next
            n+=1
        n1,n2=dummy,dummy
        i=1
        while i!=k:
            i+=1
            n1=n1.next
        i=1
        while i!=n-k:
            i+=1
            n2=n2.next
        # if n1.next and n2.next:
        #     n1.next.next,n2.next.next,n1.next,n2.next=n2.next.next,n1.next.next,n2.next,n1.next
        # else:
        #     n1.next,n2.next=n2.next,n1.next

        n1next_old=n1.next
        n2next_old=n2.next
        n1nextnext_old=n1.next.next
        n2nextnext_old=n2.next.next

        if n1next_old and n2next_old:
            n1.next.next,n2.next.next,n1.next,n2.next=n2nextnext_old,n1nextnext_old,n2next_old,n1next_old
        else:
            n1.next,n2.next=n2next_old,n1next_old
        return dummy.next



def make_linked_list(li,i=0):
    if i==len(li)-1:return ListNode(li[i])
    cur = ListNode(li[i])
    cur.next = make_linked_list(li,i+1)
    return cur
class tester(unittest.TestCase):
    def test_01(self):
        head = [1, 2, 3, 4, 5]
        head = make_linked_list(head)
        k=2
        Output = [1,4,3,2,5]
        Output = make_linked_list(Output)
        self.assertEqual(Output, get_sol().swapNodes(head,k) )
    def test_01_2(self):
        head = [1, 2, 3, 4, 5]
        head = make_linked_list(head)
        k=3
        Output = [1, 2, 3, 4, 5]
        Output = make_linked_list(Output)
        self.assertEqual(Output, get_sol().swapNodes(head,k) )
    def test_01_3(self):
        head = [1, 2, 3, 4, 5]
        head = make_linked_list(head)
        k=4
        Output = [1,4,3,2,5]
        Output = make_linked_list(Output)
        self.assertEqual(Output, get_sol().swapNodes(head,k) )
    def test_02(self):
        head = [7,9,6,6,7,8,3,0,9,5]
        head = make_linked_list(head)
        k = 5
        Output= [7,9,6,6,8,7,3,0,9,5]
        Output = make_linked_list(Output)
        self.assertEqual(Output, get_sol().swapNodes(head,k) )
    def test_03(self):
        head = [1]
        head = make_linked_list(head)
        k = 1
        Output= [1]
        Output = make_linked_list(Output)
        self.assertEqual(Output, get_sol().swapNodes(head,k) )
    def test_04(self):
        head = [1,2]
        head = make_linked_list(head)
        k = 1
        Output= [2,1]
        Output = make_linked_list(Output)
        self.assertEqual(Output, get_sol().swapNodes(head,k) )
    def test_05(self):
        head = [1,2,3]
        head = make_linked_list(head)
        k = 2
        Output= [1,2,3]
        Output = make_linked_list(Output)
        self.assertEqual(Output, get_sol().swapNodes(head,k) )
