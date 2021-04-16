from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List




class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def get_length(head:ListNode):
            if not head:return 0
            n = 0
            while head:
                n+=1
                head=head.next
            return n
        def helper(head:ListNode):
            length = get_length(head)
            if length==0:return None
            if length==1:return TreeNode(head.val)
            n=0
            curr = head
            while n!=length//2-1:
                n+=1
                curr=curr.next
            head2 = curr.next.next
            root = TreeNode(curr.next.val)
            curr.next=None
            root.left = helper(head)
            root.right = helper(head2)
            return root

        return helper(head)
