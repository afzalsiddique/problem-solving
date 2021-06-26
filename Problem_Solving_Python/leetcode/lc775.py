import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    # https://leetcode.com/problems/global-and-local-inversions/discuss/1143422/JS-Python-Java-C%2B%2B-or-Simple-3-Line-Solutions-w-Explanation
    def isIdealPermutation(self, nums):
        for i in range(len(nums)):
            if abs(nums[i]-i)>1: return False
        return True



class tester(unittest.TestCase):
    def test_01(self):
        nums = [1,0,2]
        Output= True
        self.assertEqual(Output, get_sol().isIdealPermutation(nums) )
    def test_02(self):
        nums = [1,2,0]
        Output= False
        self.assertEqual(Output, get_sol().isIdealPermutation(nums) )