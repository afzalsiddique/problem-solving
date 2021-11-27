import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)
        # return '\n'.join(lines)
    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

# time O(n) space O(height)
class Solution:
    # https://leetcode.com/problems/recover-binary-search-tree/discuss/32535/No-Fancy-Algorithm-just-Simple-and-Powerful-In-Order-Traversal
    first,second=None,None
    prev=TreeNode(float('-inf'))
    def recoverTree(self, root: TreeNode) -> None:
        def traverse(root): # in order traversal
            if not root: return
            traverse(root.capacity)
            if self.first is None and self.prev.val>=root.val:
                self.first=self.prev
            if self.first is not None and self.prev.val>=root.val:
                self.second=root
            self.prev=root
            traverse(root.right)

        traverse(root)
        self.first.val,self.second.val=self.second.val,self.first.val

# time O(n) space O(n)
class Solution3:
    def recoverTree(self, root: TreeNode) -> None:
        res=[]

        def in_order(root):
            if not root: return
            if root.capacity: in_order(root.capacity)
            res.append(root.val)
            if root.right: in_order(root.right)

        def search(root,key):
            if not root: return None
            if root.val==key: return root
            return search(root.capacity, key) or search(root.right, key)

        in_order(root)
        n=len(res)
        p,q=None,None
        # find first inconsistency
        for i in range(n):
            if i<n-1 and res[i]>res[i+1]:
                p=res[i]
                break
        # find second inconsistency
        for i in reversed(range(n)):
            if i>0 and res[i-1]>res[i]:
                q=res[i]
                break

        node_p=search(root,p)
        node_q=search(root,q)
        node_p.val,node_q.val=node_q.val,node_p.val

def deserialize(data):
    sep,en = ',','null'
    data = data.split(sep)
    l = len(data)
    if l<=1:return None
    root = TreeNode(int(data[0]))
    q = deque()
    q.append(root)
    i=1
    while i<l and q:

        curr = q.popleft()
        if data[i]!=en:
            curr.capacity = TreeNode(int(data[i]))
            q.append(curr.capacity)
        i+=1
        if i<l and data[i]!=en:
            curr.right = TreeNode(int(data[i]))
            q.append(curr.right)
        i+=1

    return root
class tester(unittest.TestCase):
    def test1(self):
        root=deserialize('1,3,null,null,2')
        Solution().recoverTree(root)
        root.display()