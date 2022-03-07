from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self): return str(self.val)

class Solution:
    # time O(n)
    # https://leetcode.com/problems/maximum-binary-tree/discuss/258364/Python-O(n)-solution-with-explanation.
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        st=[] # decreasing stack
        for num in nums:
            last=None
            while st and num>st[-1].val: # everything inside the stack is greater than num
                last=st.pop()
            node = TreeNode(num)
            if last:
                node.left = last
            if st:
                st[-1].right = node
            st.append(node)
        return st[0]


class Solution2:
    # time O(n^2)
    # with range(lo,hi)
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def helper(lo,hi):
            if lo>hi: return None
            idx,maxx=lo,float('-inf')
            for i in range(lo,hi+1):
                if nums[i]>maxx:
                    idx,maxx=i,nums[i]
            node = TreeNode(maxx)
            node.left=helper(lo,idx-1)
            node.right=helper(idx+1,hi)
            return node
        return helper(0,len(nums)-1)

# time O(n^2)
# passing copy of nums array in the recursive function
class Solution3:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def helper(nums):
            if not nums: return None
            idx,maxx=0,float('-inf')
            for i in range(len(nums)):
                if nums[i]>maxx:
                    idx,maxx=i,nums[i]
            root= TreeNode(maxx)
            root.left=helper(nums[:idx])
            root.right=helper(nums[idx+1:])
            return root

        return helper(nums)



class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual( "6,3,5,null,2,0,null,null,1" ,ser(get_sol().constructMaximumBinaryTree([3,2,1,6,0,5])))
    def test02(self):
        self.assertEqual( "3,null,2,null,1" ,ser(get_sol().constructMaximumBinaryTree([3,2,1])))
    def test03(self):
        self.assertEqual( "3,2,null,1" ,ser(get_sol().constructMaximumBinaryTree([1,2,3])))
    def test04(self):
        self.assertEqual( "5,null,4,null,3,2" ,ser(get_sol().constructMaximumBinaryTree([5,4,2,3])))
