from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(left,right): # both inclusive
            if left>right:
                return [None]
            ans=[]
            for i in range(left,right+1):
                for l in generate(left,i-1):
                    for r in generate(i+1,right):
                        node=TreeNode(i)
                        node.left=l
                        node.right=r
                        ans.append(node)
            return ans


        return generate(1,n)
class Solution2:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(left,right): # left inclusive, right exclusive
            if left==right:
                return [None]
            ans=[]
            for i in range(left,right):
                for l in generate(left,i):
                    for r in generate(i+1,right):
                        node=TreeNode(i)
                        node.left=l
                        node.right=r
                        ans.append(node)
            return ans


        return generate(1,n+1)


class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(['1,null,2,null,3', '1,null,3,2', '2,1,3', '3,1,null,null,2', '3,2,null,1'],[ser(x) for x in get_sol().generateTrees(3)])
    def test02(self):
        self.assertEqual(['1'],[ser(x) for x in get_sol().generateTrees(1)])
