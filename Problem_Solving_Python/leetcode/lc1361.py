import itertools;
import math;
import operator;
import random;
import re;
from bisect import *;
from collections import deque, defaultdict, Counter, OrderedDict;
from heapq import *;
import unittest;
from typing import List
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/validate-binary-tree-nodes/discuss/939381/Python%3A-clean-BFS-96-faster-TimeComplexity%3A-O(n)-Space-Complexity%3A-O(n)
    def validateBinaryTreeNodes(self, n: int, left: List[int], right: List[int]) -> bool:
        root = 0
        no_of_possible_roots=0
        childrenNodes = set(left + right)
        for i in range(n):
            if i not in childrenNodes:
                root = i
                no_of_possible_roots+=1
        if no_of_possible_roots!=1: return False # optimization

        visited = set()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node in visited:
                return False
            visited.add(node)
            if left[node] != -1:
                queue.append(left[node])
            if right[node] != -1:
                queue.append(right[node])

        # number of visited nodes == given number of nodes
        # if n != len(visited) => some nodes are unreachable/multiple different trees
        return len(visited) == n


class Solution2:
    def validateBinaryTreeNodes(self, n: int, left: List[int], right: List[int]) -> bool:
        vis = set()

        def dfs(node):
            if node == -1: return True
            if node in vis: return False
            vis.add(node)
            return dfs(left[node]) and dfs(right[node])

        di = {i: [] for i in range(n)}
        for par in range(n):
            child = left[par]
            if child == -1: continue
            di[child].append(par)
        for par in range(n):
            child = right[par]
            if child == -1: continue
            di[child].append(par)

        no_of_possible_roots = 0
        for child in di:
            no_of_parent = len(di[child])
            if no_of_parent == 0:
                no_of_possible_roots += 1
                root = child
            if no_of_parent > 1: return False
        if no_of_possible_roots != 1: return False
        return dfs(root) and len(vis) == n


class tester(unittest.TestCase):
    def test_1(self):
        n, leftChild, rightChild = 4, [1, -1, 3, -1], [2, -1, -1, -1]
        Output = True
        self.assertEqual(Output, get_sol().validateBinaryTreeNodes(n, leftChild, rightChild))
    def test_2(self):
        n, leftChild, rightChild = 4, [1, -1, 3, -1], [2, 3, -1, -1]
        Output = False
        self.assertEqual(Output, get_sol().validateBinaryTreeNodes(n, leftChild, rightChild))
    def test_3(self):
        n, leftChild, rightChild = 2, [1, 0], [-1, -1]
        Output = False
        self.assertEqual(Output, get_sol().validateBinaryTreeNodes(n, leftChild, rightChild))
    def test_4(self):
        n, leftChild, rightChild = 6, [1, -1, -1, 4, -1, -1], [2, -1, -1, 5, -1, -1]
        Output = False
        self.assertEqual(Output, get_sol().validateBinaryTreeNodes(n, leftChild, rightChild))
    def test_5(self):
        n, leftChild, rightChild = 4, [3, -1, 1, -1], [-1, -1, 0, -1]
        Output = True
        self.assertEqual(Output, get_sol().validateBinaryTreeNodes(n, leftChild, rightChild))
    def test_6(self):
        n, leftChild, rightChild = 4, [1, 0, 3, -1], [-1, -1, -1, -1]
        Output = False
        self.assertEqual(Output, get_sol().validateBinaryTreeNodes(n, leftChild, rightChild))
    def test_7(self):
        n, leftChild, rightChild = 4, [1, 2, 0, -1], [-1, -1, -1, -1]
        Output = False
        self.assertEqual(Output, get_sol().validateBinaryTreeNodes(n, leftChild, rightChild))
    def test_8(self):
        n, leftChild, rightChild = 3, [1, -1, 0], [-1, -1, -1]
        Output = True
        self.assertEqual(Output, get_sol().validateBinaryTreeNodes(n, leftChild, rightChild))
