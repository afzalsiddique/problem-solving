import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self): return str(self.val) + "->" + str(self.next)
# class Solution2:
#     def nextLargerNodes(self, head: ListNode) -> List[int]:
        # maybe it is possible to do it in one pass
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        node=head
        i=0
        while node:
            i+=1
            node=node.next
        n=i # length of the linked list

        st=[]
        res=[0]*n
        for i in range(n):
            while st and head.val>st[-1][1]:
                tmp_idx,val = st.pop()
                res[tmp_idx]=head.val
            st.append((i,head.val))
            head=head.next
        return res


def make_linked_list(li,i=0):
    if i==len(li)-1:return ListNode(li[i])
    cur = ListNode(li[i])
    cur.next = make_linked_list(li,i+1)
    return cur
class tester(unittest.TestCase):
    def test_1(self):
        Input= [2,1,5]
        Output= [5,5,0]
        Input = make_linked_list(Input)
        self.assertEqual(Output, get_sol().nextLargerNodes(Input))
    def test_2(self):
        Input= [2,7,4,3,5]
        Output= [7,0,5,5,0]
        Input = make_linked_list(Input)
        self.assertEqual(Output, get_sol().nextLargerNodes(Input))
    def test_3(self):
        Input= [1,7,5,1,9,2,5,1]
        Output= [7,9,9,9,0,5,0,0]
        Input = make_linked_list(Input)
        self.assertEqual(Output, get_sol().nextLargerNodes(Input))
