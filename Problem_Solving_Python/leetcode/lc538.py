from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)

class Solution:
    # https://www.youtube.com/watch?v=GX3X5Ami8L8
    summ=0
    def convertBST(self, root: TreeNode) -> TreeNode:
        def traverse(root):
            if not root: return
            traverse(root.right)
            self.summ+=root.val
            root.val=self.summ
            traverse(root.left)

        traverse(root)
        return root

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(ser(des([30,36,21,36,35,26,15,None,None,None,33,None,None,None,8])),ser(get_sol().convertBST(des([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]))))
    def test02(self):
        self.assertEqual(ser(des([1,None,1])),ser(get_sol().convertBST(des([0,None,1]))))
    def test03(self):
        self.assertEqual(ser(des([3,3,2])),ser(get_sol().convertBST(des([1,0,2]))))
    def test04(self):
        self.assertEqual(ser(des([7,9,4,10])),ser(get_sol().convertBST(des([3,2,4,1]))))
