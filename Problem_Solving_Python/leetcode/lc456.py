import itertools
import math
import random
from bisect import *
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()


class Solution:
    # time O(n) memory O(n)
    # https://leetcode.com/problems/132-pattern/discuss/94089/Java-solutions-from-O(n3)-to-O(n)-for-%22132%22-pattern-(updated-with-one-pass-slution)
    # https://www.youtube.com/watch?v=xV-QDXn9Brc
    def find132pattern(self, nums: List[int]) -> bool:
        n=len(nums)
        min_list = list(itertools.accumulate(nums,min))
        st=[]
        for j in reversed(range(n)):
            numsi=min_list[j]
            while st and st[-1]<=numsi:
                st.pop()
            if st and numsi<st[-1]<nums[j]: return True
            st.append(nums[j])
        return False

class Solution2:
    # https://leetcode.com/problems/132-pattern/discuss/94089/Java-solutions-from-O(n3)-to-O(n)-for-%22132%22-pattern-(updated-with-one-pass-slution)
    def find132pattern(self, nums: List[int]) -> bool:
        n=len(nums)
        numsi=float('inf')
        for j in range(n-1):
            numsi = min(numsi,nums[j])
            if numsi==nums[j]: continue # choose a different j
            for k in range(j+1,n):
                if numsi<nums[k]<nums[j]: return True
        return False

class Tester(unittest.TestCase):
    def test01(self):
        nums = [1,2,3,4]
        Output= False
        self.assertEqual(Output,get_sol().find132pattern(nums))
    def test02(self):
        nums = [3,1,4,2]
        Output= True
        self.assertEqual(Output,get_sol().find132pattern(nums))
    def test03(self):
        nums = [-1,3,2,0]
        Output= True
        self.assertEqual(Output,get_sol().find132pattern(nums))
    def test04(self):
        nums = [1,0,1,-4,-3]
        Output= False
        self.assertEqual(Output,get_sol().find132pattern(nums))
    def test05(self):
        self.assertEqual(True,get_sol().find132pattern([3,5,0,3,4]))
