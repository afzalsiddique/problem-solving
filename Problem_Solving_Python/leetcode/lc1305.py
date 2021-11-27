import itertools
import math
import operator
import random
from bisect import *
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class Solution:
    # https://leetcode.com/problems/all-elements-in-two-binary-search-trees/discuss/464368/Short-O(n)-Python
    def getAllElements(self, root1, root2):
        values = []
        def collect(root):
            if root:
                collect(root.left)
                values.append(root.val)
                collect(root.right)
        collect(root1)
        collect(root2)
        # sorting used here is tim sort which has a best case complexity of O(n).
        return sorted(values)
