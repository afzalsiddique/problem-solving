import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# time O(n)
class Solution:
    # https://leetcode.com/problems/maximum-binary-tree/discuss/258364/Python-O(n)-solution-with-explanation.
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        st=[]
        last=None
        for num in nums:
            while st and num>st[-1].val:
                last=st.pop()
            node = TreeNode(num)
            if last:
                node.left = last
            if st:
                st[-1].right = node
            last = None
            st.append(node)
        return st[0]


# time O(n^2)
# with range(lo,hi)
class Solution2:
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

def serialize(root):
    en = 'null'
    sep = ','
    if not root: return ''
    q = deque()
    res = [str(root.val)]
    q.append(root)
    while q:
        cur = q.popleft()
        for child in [cur.left, cur.right]:
            if child:
                q.append(child)
                res.append(str(child.val))
            else:
                res.append(en)
    return sep.join(res)

class mytestcase(unittest.TestCase):
    def test1(self):
        self.assertEqual( "6,3,5,null,2,0,null,null,1" ,serialize(Solution().constructMaximumBinaryTree([3,2,1,6,0,5])))
    def test2(self):
        self.assertEqual( "3,null,2,null,1" ,serialize(Solution().constructMaximumBinaryTree([3,2,1])))
    def test3(self):
        self.assertEqual( "###" ,serialize(Solution().constructMaximumBinaryTree([1,2,3])))
