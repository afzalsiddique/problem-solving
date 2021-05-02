import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List



class Solution:
    # time O(n) space O(n)
    def findMaxLength(self, nums: List[int]) -> int:
        maxx=0
        summ=0
        di={0:-1}
        for i,num in enumerate(nums):
            if num==1: summ+=1
            else: summ-=1
            if summ not in di:
                di[summ]=i
            else:
                maxx=max(maxx,i-di[summ])
        return maxx


class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(2,Solution().findMaxLength([1,0]))
    def test2(self):
        self.assertEqual(2,Solution().findMaxLength([0,1,0]))
    def test3(self):
        self.assertEqual(6,Solution().findMaxLength([0,0,1,0,0,0,1,1]))
