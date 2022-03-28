from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        lines, *_ = self._display_aux()
        # for line in lines:
        #     print(line)
        return '\n'.join(lines)

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


class Solution:
    def generateTrees(self, n):
        def helper(li):
            if not li: return [None]
            res=[]
            for i in range(len(li)):
                for left in helper(li[:i]):
                    for right in helper(li[i + 1:]):
                        node, node.left, node.right= TreeNode(li[i]), left, right
                        res+=[node]
            return res

        res = helper([i for i in range(1, n+1)])
        for r in res:
            print(r)
            print()
        return res

# same as above but with left and right range
class Solution2:
    def generateTrees(self, n):
        return self.dfs(1, n+1)

    def dfs(self, start, end):
        if start == end:
            return [None]
        result = []
        for i in range(start, end):
            for l in self.dfs(start, i):
                for r in self.dfs(i+1, end):
                    node = TreeNode(i)
                    node.left, node.right  = l, r
                    result.append(node)
        return result


class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(['1,null,2,null,3', '1,null,3,2', '2,1,3', '3,1,null,null,2', '3,2,null,1'],[ser(x) for x in get_sol().generateTrees(3)])
