from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self): return str(self.val)+'->'+str(self.next)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1=self.reverseList(l1)
        r2=self.reverseList(l2)
        node=self.add(r1,r2,0)
        return self.reverseList(node)
    def add(self,node1,node2,carry): # leetcode 2
        if not node1 and not node2:
            if not carry:
                return None
            return ListNode(carry)
        val1=node1.val if node1 else 0
        val2=node2.val if node2 else 0
        val=val1+val2+carry
        carry=val//10
        val=val%10
        node=ListNode(val)
        node.next=self.add(node1.next if node1 else None,node2.next if node2 else None,carry)
        return node
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return head
        ret=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return ret
# two stacks
class Solution3:
    def addTwoNumbers(self, l1, l2):
        st1, st2 = [], []
        while l1:
            st1.append(l1.val)
            l1 = l1.next
        while l2:
            st2.append(l2.val)
            l2 = l2.next

        carry, head = 0, None
        while st1 or st2 or carry:
            d1 = st1.pop() if st1 else 0
            d2 = st2.pop() if st2 else 0
            carry, digit = divmod(d1 + d2 + carry, 10)
            head_new = ListNode(digit)
            head_new.next = head
            head = head_new

        return head

class Solution2:
    def make_linked_list(self,li,i=0):
        if i==len(li)-1:return ListNode(li[i])
        cur = ListNode(li[i])
        cur.next = self.make_linked_list(li,i+1)
        return cur
    def extract_number(self,head,res):
        if not head: return
        res.append(head.val)
        self.extract_number(head.next,res)
    def add_two(self,li1,li2):
        res=[0]*(1+max(len(li1),len(li2)))
        i,j,k=len(li1)-1,len(li2)-1,len(res)-1
        carry=0
        while i>=0 and j>=0:
            cur=li1[i]+li2[j]+carry
            res[k]=cur%10
            carry=cur//10
            i-=1;j-=1;k-=1
        while i>=0:
            cur=li1[i]+carry
            res[k]=cur%10
            carry=cur//10
            i-=1;k-=1
        while j>=0:
            cur=li2[j]+carry
            res[k]=cur%10
            carry=cur//10
            j-=1;k-=1
        res[0]=carry
        k=0
        while k<len(res) and res[k]==0: k+=1
        if res[k:]:
            return res[k:]
        return [0] # l1=[0],l2[0]
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        li1,li2=[],[]
        self.extract_number(l1,li1)
        self.extract_number(l2,li2)
        res=self.add_two(li1,li2)
        head=self.make_linked_list(res)
        return head
class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(make_linked_list([7,8,0,7]),get_sol().addTwoNumbers(make_linked_list([7,2,4,3]),make_linked_list([5,6,4])))
    def test02(self):
        self.assertEqual(make_linked_list([8,0,7]),get_sol().addTwoNumbers(make_linked_list([2,4,3]),make_linked_list([5,6,4])))
    def test03(self):
        self.assertEqual(make_linked_list([0]),get_sol().addTwoNumbers(make_linked_list([0]),make_linked_list([0])))
    # def test04(self):
    # def test05(self):
