from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)+'->'+str(self.next)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        head=dummy
        carry=0
        while l1 or l2:
            a=l1.val if l1 else 0
            b=l2.val if l2 else 0
            val=a+b+carry
            head.next=ListNode(val%10)
            carry=val//10
            head=head.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        if carry:
            head.next=ListNode(carry)


        return dummy.next
class Solution5:
    def get_num(self,head):
        if head is None: return 0
        return self.get_num(head.next) * 10 + head.val
    def make_linked_list(self,li,i=0):
        if i==len(li)-1:return ListNode(li[i])
        cur = ListNode(li[i])
        cur.next = self.make_linked_list(li,i+1)
        return cur
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        summ = self.get_num(l1) + self.get_num(l2)
        li = [int(c) for c in str(summ)]
        li = li[::-1]
        head = self.make_linked_list(li,0)
        return head
class Solution6:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def recur(node1,node2,carry):
            if not node1 and not node2:
                if carry:
                    return ListNode(carry)
                return None
            val1=node1.val if node1 else 0
            val2=node2.val if node2 else 0
            val=val1+val2+carry
            node=ListNode(val%10)
            carry=val//10
            node.next=recur(node1.next if node1 else None,node2.next if node2 else None,carry)
            return node

        return recur(l1,l2,0)


class Solution3:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def extract_val(cur):
            if not cur:return 0
            if not cur.next:return cur.val
            return cur.val  + extract_val(cur.next)* 10
        def create_linked_list(nums):
            head = None
            for val in nums:
                nxt = ListNode(val)
                nxt.next = head
                head = nxt
            return head
        num1 = extract_val(l1)
        num2 = extract_val(l2)
        ans = str(num1+num2)
        nums = [int(ch) for ch in ans]
        return create_linked_list(nums)
class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def get_int_val(head:ListNode):
            mul=1
            ans = 0
            while head:
                ans+=head.val*mul
                mul*=10
                head=head.next
            return ans
        def make_linked_list(num:int):
            if num==0:return ListNode(0)
            li = []
            while num:
                digit = num%10
                li.append(digit)
                num=num//10
            li.reverse()
            prev=ListNode(li[0])
            for i in range(1,len(li)):
                curr = ListNode(li[i], prev)
                prev = curr
            return prev
        first = get_int_val(l1)
        second = get_int_val(l2)
        summ = first+second
        head = make_linked_list(summ)
        return head



class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(make_linked_list([7,0,8]),get_sol().addTwoNumbers(make_linked_list([2,4,3]),make_linked_list([5,6,4])))
    def test02(self):
        self.assertEqual(make_linked_list([0]),get_sol().addTwoNumbers(make_linked_list([0]),make_linked_list([0])))
    def test03(self):
        self.assertEqual(make_linked_list([8,9,9,9,0,0,0,1]),get_sol().addTwoNumbers(make_linked_list([9,9,9,9,9,9,9]),make_linked_list([9,9,9,9])))
    def test04(self):
        self.assertEqual(make_linked_list([6,5,5,6,4,4,2,5,5,1]),get_sol().addTwoNumbers(make_linked_list([0,8,6,5,6,8,3,5,7]),make_linked_list([6,7,8,0,8,5,8,9,7])))
    # def test05(self):
