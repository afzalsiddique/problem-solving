import itertools;from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        TAKE,SKIP=True,False
        @cache
        def func(node:TreeNode,state:bool)->int:
            if not node: return 0
            l1,l2,r1,r2=float('-inf'),float('-inf'),float('-inf'),float('-inf')
            res=0
            if state==TAKE:
                l1=func(node.left,SKIP)
                r1=func(node.right,SKIP)
                res+=node.val
            else:
                l1=func(node.left,SKIP)
                r1=func(node.right,SKIP)
                l2=func(node.left,TAKE)
                r2=func(node.right,TAKE)
            res+=max(l1,l2)+max(r1,r2)
            return res

        return max(func(root,TAKE),func(root,SKIP))

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(7,Solution().rob(des([3,2,3,None,3,None,1])))
    def test02(self):
        self.assertEqual(9,Solution().rob(des([3,4,5,1,3,None,1])))
    def test03(self):
        self.assertEqual(8,Solution().rob(des([4,2,None,1,3])))
    def test04(self):
        self.assertEqual(3038,Solution().rob(des([79,99,77,None,None,None,69,None,60,53,None,73,11,None,None,None,62,27,62,None,None,98,50,None,None,90,48,82,None,None,None,55,64,None,None,73,56,6,47,None,93,None,None,75,44,30,82,None,None,None,None,None,None,57,36,89,42,None,None,76,10,None,None,None,None,None,32,4,18,None,None,1,7,None,None,42,64,None,None,39,76,None,None,6,None,66,8,96,91,38,38,None,None,None,None,74,42,None,None,None,10,40,5,None,None,None,None,28,8,24,47,None,None,None,17,36,50,19,63,33,89,None,None,None,None,None,None,None,None,94,72,None,None,79,25,None,None,51,None,70,84,43,None,64,35,None,None,None,None,40,78,None,None,35,42,98,96,None,None,82,26,None,None,None,None,48,91,None,None,35,93,86,42,None,None,None,None,0,61,None,None,67,None,53,48,None,None,82,30,None,97,None,None,None,1,None,None])))
