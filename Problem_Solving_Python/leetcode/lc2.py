from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)+','+str(self.next)
class Solution:
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


class tester(unittest.TestCase):
    def test1(self):
        l1,l2=Solution().make_linked_list([2,4,3]),Solution().make_linked_list([5,6,4])
        expected = Solution().make_linked_list([7,0,8])
        self.assertEqual(str(expected),str(Solution().addTwoNumbers(l1,l2)))
