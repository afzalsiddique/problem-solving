from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(lo,hi):
            if lo>hi:return None
            mid = (lo+hi)//2
            root = TreeNode(nums[mid])
            root.left=helper(lo,mid-1)
            root.right = helper(mid+1,hi)
            return root


        return helper(0,len(nums)-1)
