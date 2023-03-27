from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution2()
class Solution:
    # https://www.youtube.com/watch?v=VwylCVAVdmo
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        @cache
        def canSplit(i:int,num_left:int, sum_left:int):
            if num_left==0:
                return not sum_left
            return canSplit(i+1,num_left-1,sum_left-nums[i]) or canSplit(i+1,num_left,sum_left)

        n=len(nums)
        S=sum(nums)
        for num_selected in range(1,n):
            target_sum=S*num_selected/n
            if floor(target_sum)==ceil(target_sum): # if it is integer
                if canSplit(0,num_selected,int(target_sum)):
                    return True
        return False

class Solution2:
    # https://www.youtube.com/watch?v=VwylCVAVdmo
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        @cache
        def canSplit(i,nums_left,sum_left):
            if not nums_left:
                return sum_left==0
            if i==n: return False
            if canSplit(i+1,nums_left-1,sum_left-nums[i]):
                return True
            if canSplit(i+1,nums_left,sum_left):
                return True
            return False

        n=len(nums)
        S=sum(nums)
        for num_selected in range(1,n):
            target_sum=S*num_selected/n
            if floor(target_sum)==ceil(target_sum): # if it is integer
                if canSplit(0,num_selected,target_sum):
                    return True
        return False


class Tester(unittest.TestCase):
    def test_1(self):
        self.assertEqual(True,get_sol().splitArraySameAverage(nums = [1,2,3,4,5,6,7,8]))
    def test_2(self):
        self.assertEqual(False,get_sol().splitArraySameAverage(nums = [3,1]))
    def test_3(self):
        self.assertEqual(False,get_sol().splitArraySameAverage(nums = [60,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]))
    def test_4(self):
        self.assertEqual(False,get_sol().splitArraySameAverage(nums = [3863,703,1799,327,3682,4330,3388,6187,5330,6572,938,6842,678,9837,8256,6886,2204,5262,6643,829,745,8755,3549,6627,1633,4290,7]))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
