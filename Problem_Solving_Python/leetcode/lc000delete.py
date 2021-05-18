import itertools
import math
import operator
import random
from bisect import *
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
# def get_sol(): return Solution()


class Solution2:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        subtrees=defaultdict(list)
        def helper(node:TreeNode)-> (int,int):
            if not node: return 0,0
            left_size,left_depth=helper(node.left)
            right_size,right_depth=helper(node.right)
            size=1+left_size+right_size
            depth=1+max(left_depth,right_depth)
            subtrees[node].append(depth) # depth at 0th index
            subtrees[node].append(size) # size at 1st index
            return size,depth

        helper(root)
        li = sorted(subtrees.values(),key=lambda x:(-x[1],x[0]))
        print(li)
