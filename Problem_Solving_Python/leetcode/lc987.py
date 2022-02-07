from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# https://www.youtube.com/watch?v=kqHNP6NTzME&t=4m51s

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def helper(node:TreeNode, row:int,col:int):
            if node is None:return

            di[col].append((node.val,row))
            helper(node.left, row + 1,col-1)
            helper(node.right, row + 1,col+1)
            return


        di = defaultdict(list)
        helper(root,0,0)
        result = []
        for x in sorted(di.keys()):
            temp = sorted(di[x],key=lambda x:(x[1],x[0]))# sort based on row and then val
            result.append([item[0] for item in temp])

        return result
class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([[9],[3,15],[20],[7]],get_sol().verticalTraversal(des([3,9,20,None,None,15,7])))
    def test2(self):
        self.assertEqual([[4],[2],[1,5,6],[3],[7]],get_sol().verticalTraversal(des([1,2,3,4,5,6,7])))
    def test3(self):
        self.assertEqual([[4],[2],[1,5,6],[3],[7]],get_sol().verticalTraversal(des([1,2,3,4,6,5,7])))
    def test4(self):
        self.assertEqual([[0],[1],[3,2,2],[4]],get_sol().verticalTraversal(des([3,1,4,0,2,2])))
