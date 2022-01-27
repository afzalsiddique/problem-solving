from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()
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
    def createArray(self,head):
        li=[]
        while head:
            li.append(head.val)
            head=head.next
        return li
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def helper(l,r):
            if l>r: return None
            mid=(l+r)//2
            return TreeNode(nums[mid],helper(l,mid-1),helper(mid+1,r))

        nums=self.createArray(head)
        return helper(0,len(nums)-1)
class Solution2:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def get_length(head:ListNode):
            if not head:return 0
            n = 0
            while head:
                n+=1
                head=head.next
            return n
        def helper(leftHead:ListNode):
            length = get_length(leftHead)
            if length==0:return None
            if length==1:return TreeNode(leftHead.val)
            n=0
            curr = leftHead
            while n!=length//2-1:
                n+=1
                curr=curr.next
            rightHead = curr.next.next
            root = TreeNode(curr.next.val)
            curr.next=None
            root.left = helper(leftHead)
            root.right = helper(rightHead)
            return root

        return helper(head)

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertIn(ser(get_sol().sortedListToBST(make_linked_list([-10,-3,0,5,9]))),['0,-3,9,-10,null,5','0,-10,5,null,-3,null,9'])
    def test02(self):
        self.assertEqual(None,get_sol().sortedListToBST(make_linked_list([])))
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
