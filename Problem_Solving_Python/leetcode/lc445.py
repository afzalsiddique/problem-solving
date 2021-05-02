import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)+','+str(self.next)
    def __eq__(self, other):
        return str(self)==str(other)
# two stacks
class Solution:
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
def make_linked_list(li,i=0):
    if i==len(li)-1:return ListNode(li[i])
    cur = ListNode(li[i])
    cur.next = make_linked_list(li,i+1)
    return cur
class tester(unittest.TestCase):
    def test1(self):
        l1=make_linked_list([9,9,9])
        l2=make_linked_list([9,9,9])
        res=make_linked_list([1,9,9,8])
        self.assertEqual(res,Solution().addTwoNumbers(l1,l2))
    def test2(self):
        l1=make_linked_list([7,2,4,3])
        l2=make_linked_list([5,6,4])
        res=make_linked_list([7,8,0,7])
        self.assertEqual(res,Solution().addTwoNumbers(l1,l2))
    def test3(self):
        l1=make_linked_list([2,4,3])
        l2=make_linked_list([5,6,4])
        res=make_linked_list([8,0,7])
        self.assertEqual(res,Solution().addTwoNumbers(l1,l2))
    def test4(self):
        l1=make_linked_list([0])
        l2=make_linked_list([0])
        res=make_linked_list([0])
        self.assertEqual(res,Solution().addTwoNumbers(l1,l2))