from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()
###### UNIQUE BINARY TREE IS NOT POSSIBLE #####
###### ANY VALID BINARY TREE IS ACCEPTABLE #####
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    # pre
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def helper(start, end):
            nonlocal i
            if start>end: return None

            if start==end:
                node= TreeNode(pre[i])
                i+=1
                return node

            node=TreeNode(pre[i])
            i+=1
            mid=idx[pre[i]]
            node.left= helper(start , mid)
            node.right= helper(mid+1, end-1)
            return node

        n=len(pre)
        idx={x:i for i,x in enumerate(post)}
        i=0
        return helper(0, n-1)
class Solution6:
    # https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/discuss/748216/Python3-Solution-with-a-Detailed-Explanation-Construct-Binary-Tree-from/986020
    # post order
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def helper(start, end):
            nonlocal i
            if end<start: return None

            if start==end:
                node= TreeNode(post[i])
                i-=1
                return node

            node=TreeNode(post[i])
            i-=1
            mid=idx[post[i]]
            node.right= helper(mid, end)
            node.left= helper(start + 1, mid-1)
            return node

        n=len(pre)
        idx={x:i for i,x in enumerate(pre)}
        i=n-1
        return helper(0, n-1)
class Solution4:
    # https://www.youtube.com/watch?v=LnHSOy7ctms
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def helper(post):
            nonlocal i
            if not post: return None
            root = TreeNode(pre[i])
            i+=1
            if len(post)==1: return root
            idx = post.index(pre[i]) # using dictionary will reduce time complexity

            left = post[:idx+1]
            right = post[idx+1:-1]

            root.left = helper(left)
            root.right = helper(right)
            return root

        i=0
        return helper(post)

class Solution2:
    def constructFromPrePost(self, pre, post):
        def helper(pre,post):
            if not pre: return None
            root = TreeNode(pre[0])
            if len(post) == 1: return root
            idx = pre.index(post[-2]) # using dictionary will reduce time complexity
            root.left = helper(pre[1: idx], post[:(idx - 1)])
            root.right = helper(pre[idx: ], post[(idx - 1):-1])
            return root

        return helper(pre,post)

class Solution3:
    def constructFromPrePost(self, pre, post):
        def helper(pre,post):
            if not pre: return None
            root = TreeNode(pre[0])
            if len(pre) == 1: return root
            idx = post.index(pre[1]) # using dictionary will reduce time complexity
            root.left = helper(pre[1: idx+2], post[:idx+1])
            root.right = helper(pre[idx+2:], post[idx+1:-1])
            return root

        return helper(pre,post)

class Solution5:
    # wrong
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def helper(pre,post):
            if not pre: return None
            root = TreeNode(pre[0])
            if len(pre)==1: return root
            post_idx = post.index(pre[1])
            pre_idx = pre.index(post[-2])
            left_pre = pre[1:pre_idx]
            right_pre = pre[pre_idx:]
            left_post = post[:post_idx+1]
            right_post = post[post_idx+1:-1]

            root.left = helper(left_pre, left_post)
            root.right = helper(right_pre,right_post)
            return root

        return helper(pre,post)



class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual('1,2,3,4,5,6,7',ser(get_sol().constructFromPrePost([1,2,4,5,3,6,7], [4,5,2,6,7,3,1])))
    def test02(self):
        self.assertEqual('1',ser(get_sol().constructFromPrePost([1],[1])))
    def test03(self):
        self.assertIn(ser(get_sol().constructFromPrePost([2,1,3], [3,1,2])),['2,1,null,3','2,null,1,null,3'])
    # def test04(self):
    # def test05(self):
