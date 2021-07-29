# https://www.youtube.com/watch?v=quAS1iydq7U
import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()

class Solution:
    # code for PREVIOUS PERMUTATION
    def prevPermutation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        k='nothing'
        for i in reversed(range(n)):
            if i>0 and nums[i]<nums[i-1]:
                k=i-1
                break
        if k=='nothing':
            nums.reverse()
            return nums

        for l in reversed(range(n)):
            if nums[l]<nums[k]:
                break

        nums[l],nums[k]=nums[k],nums[l]
        nums[k+1:]=reversed(nums[k+1:])
        return nums

    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n=len(arr)
        k='nothing'
        for i in reversed(range(n)):
            if i>0 and arr[i]<arr[i - 1]:
                k=i-1
                break
        if k=='nothing':
            # arr.reverse() # change here
            return arr

        for l in reversed(range(n)):
            # If there are duplicate largest nums, keep decrementing j until you reach the leftmost idx of the duplicates.
            if arr[l]<arr[k] and arr[l]!=arr[l-1]: # change here # example [6, 2, 3, 0, 0, 0, 1, 1, 1, 4, 5]
                break

        arr[l], arr[k]= arr[k], arr[l]
        # arr[k + 1:]=reversed(arr[k + 1:]) # change here
        return arr

class MyTestCase(unittest.TestCase):
    def test_visualization(self):
        arr =   [6, 2, 3, 0, 0, 0, 1, 1, 1, 4, 5]
        Output= [6, 2, 1, 0, 0, 0, 3, 1, 1, 4, 5]
        self.assertEqual(Output, get_sol().prevPermOpt1(arr))
    def test_1(self):
        nums = [1,4,2,3,5]
        expected = [1,3,5,4,2]
        self.assertEqual(expected, get_sol().prevPermutation(nums))
    def test_2(self):
        nums = [1,5,1]
        expected = [1,1,5]
        self.assertEqual(expected, get_sol().prevPermutation(nums))
    def test_3(self):
        nums = [1,2,3]
        expected = [3,2,1]
        self.assertEqual(expected, get_sol().prevPermutation(nums))
    def test_4(self):
        nums = [1,3,2]
        expected = [1,2,3]
        self.assertEqual(expected, get_sol().prevPermutation(nums))
    def test_5(self):
        nums = [1]
        expected = [1]
        self.assertEqual(expected, get_sol().prevPermutation(nums))
    def test_6(self):
        nums = [2,1,3]
        expected = [1,3,2]
        self.assertEqual(expected, get_sol().prevPermutation(nums))
    def test_7(self):
        nums = [5,1,1]
        expected = [1,5,1]
        self.assertEqual(expected, get_sol().prevPermutation(nums))
    def test_8(self):
        nums = [6,2,3,0,1,4,5]
        expected = [6,2,1,5,4,3,0]
        self.assertEqual(expected, get_sol().prevPermutation(nums))
    def test_9(self):
        nums = [6,2,3,0,1,3,4,5]
        expected = [6,2,1,5,4,3,3,0]
        self.assertEqual(expected, get_sol().prevPermutation(nums))
    def test_10(self):
        nums = [6,2,3,0,1,4,5,5]
        expected = [6,2,1,5,5,4,3,0]
        self.assertEqual(expected, get_sol().prevPermutation(nums))
    def test2_1(self):
        arr = [3,2,1]
        Output= [3,1,2]
        self.assertEqual(Output, get_sol().prevPermOpt1(arr))
    def test2_2(self):
        arr = [1,1,5]
        Output= [1,1,5]
        self.assertEqual(Output, get_sol().prevPermOpt1(arr))
    def test2_3(self):
        arr = [1,9,4,6,7]
        Output= [1,7,4,6,9]
        self.assertEqual(Output, get_sol().prevPermOpt1(arr))
    def test2_4(self):
        arr =   [3,1,1,3]
        Output= [1,3,1,3]
        self.assertEqual(Output, get_sol().prevPermOpt1(arr))
    def test2_5(self):
        arr =   [3,1,1,1,1,1,1,3]
        Output= [1, 3, 1, 1, 1, 1, 1, 3]
        self.assertEqual(Output, get_sol().prevPermOpt1(arr))
    def test2_6(self):
        arr =   [5,3,1,1,1,1,1,1,3,4]
        Output= [5,1,3,1,1,1,1,1,3,4]
        self.assertEqual(Output, get_sol().prevPermOpt1(arr))
    def test2_7(self):
        arr = [5,3,1,1,3]
        Output= [5, 1, 3, 1, 3]
        self.assertEqual(Output, get_sol().prevPermOpt1(arr))
