from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, nums:List, k):
        di = defaultdict(int)
        n,res=len(nums),[]
        if k>n:return []
        if k==n:
            return [len((set(nums)))]
        for i in range(k-1):
            di[nums[i]]+=1
        for i in range(n-k+1):
            right=nums[i+k-1]
            left=nums[i]
            di[right]+=1
            res.append(len(di))
            di[left]-=1
            if di[left]==0:
                di.pop(left)
        return res
class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([2, 3, 3, 2],Solution().dNums([1, 2, 1, 3, 4, 3],3))
    def test2(self):
        self.assertEqual([1],Solution().dNums([87],1))
