from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List
import random





# Time Complexity: O(N)
# Space Complexity: O(N)
# https://www.youtube.com/watch?v=4fiDs7CCxkc
class   TreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right
class Info:
    def __init__(self):
        self.isValid = True
        self.size = 0
        self.min = 1e9
        self.max = -1e9

    def __del__(self):
        del self


def get_info(currNode, maxBST):

    if currNode == None: # if there is no node in the tree
        newInfo = Info()
        return newInfo


    left_info = get_info(currNode.left, maxBST)
    right_info = get_info(currNode.right, maxBST)


    cur_info = Info()

    cur_info.size = left_info.size + right_info.size + 1

    cur_info.isValid = left_info.isValid & right_info.isValid
    cur_info.isValid &= (currNode.data > left_info.max)
    cur_info.isValid &= (currNode.data < right_info.min)

    cur_info.min = min(min(left_info.min, right_info.min), currNode.data)
    cur_info.max = max(max(left_info.max, right_info.max), currNode.data)


    if cur_info.isValid == True:
        maxBST[0] = max(maxBST[0], cur_info.size)

    return cur_info


def largestBST(root):

    # Passing 'maxBST' by reference
    maxBST = [0]
    get_info(root, maxBST)

    return maxBST[0]


# Time Complexity: O(N^^2)
# Space Complexity: O(N)
# brute force
class   TreeNode2 :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right
def valid(root,left,right):
    if not root: return True
    if root.data <left or root.data > right:
        return False
    left = valid(root.left, left, root.data - 1)
    right = valid(root.right, root.data + 1, right)
    return left and right
def size(root):
    if not root:return 0
    return 1+size(root.left)+size(root.right)
def largestBST2(root):
    if valid(root,float('-inf'),float('inf')):
        return size(root)

    return max(largestBST2(root.left), largestBST2(root.right))

# class MyTestCase(unittest.TestCase):
#     def test1(self):
